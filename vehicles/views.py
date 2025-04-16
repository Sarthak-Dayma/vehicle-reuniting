from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q
from django.http import JsonResponse
from django.template.loader import render_to_string

from .models import FoundVehicle, LostVehicle, VehicleMatch
from .forms import FoundVehicleForm, LostVehicleForm

def home(request):
    return render(request, 'vehicles/home.html')

def report_found(request):
    if request.method == 'POST':
        form = FoundVehicleForm(request.POST, request.FILES)
        if form.is_valid():
            found_vehicle = form.save()
            
            # Check for matches immediately after saving
            check_for_matches(found_vehicle)
            
            messages.success(request, 'Thank you for reporting this vehicle. If a match is found, the owner will be notified.')
            return redirect('dashboard')
    else:
        form = FoundVehicleForm()
    
    return render(request, 'vehicles/report_found.html', {'form': form})

def report_lost(request):
    if request.method == 'POST':
        form = LostVehicleForm(request.POST, request.FILES)
        if form.is_valid():
            lost_vehicle = form.save()
            
            # Check for matches immediately after saving
            check_for_matches_with_lost(lost_vehicle)
            
            messages.success(request, 'Your vehicle has been registered as lost. You will be notified if someone reports finding it.')
            return redirect('dashboard')
    else:
        form = LostVehicleForm()
    
    return render(request, 'vehicles/report_lost.html', {'form': form})

def dashboard(request):
    search_term = request.GET.get('search', '')
    
    if search_term:
        found_vehicles = FoundVehicle.objects.filter(
            Q(make__icontains=search_term) | 
            Q(model__icontains=search_term) | 
            Q(color__icontains=search_term) | 
            Q(license_plate__icontains=search_term) |
            Q(location__icontains=search_term)
        )
        
        lost_vehicles = LostVehicle.objects.filter(
            Q(make__icontains=search_term) | 
            Q(model__icontains=search_term) | 
            Q(color__icontains=search_term) | 
            Q(license_plate__icontains=search_term) |
            Q(last_seen_location__icontains=search_term)
        )
    else:
        found_vehicles = FoundVehicle.objects.all()
        lost_vehicles = LostVehicle.objects.all()
    
    matched_vehicles = FoundVehicle.objects.filter(status='matched')
    
    context = {
        'found_vehicles': found_vehicles,
        'lost_vehicles': lost_vehicles,
        'matched_vehicles': matched_vehicles,
        'search_term': search_term
    }
    
    return render(request, 'vehicles/dashboard.html', context)

def check_for_matches(found_vehicle):
    """Check if a found vehicle matches any lost vehicles"""
    # Look for lost vehicles with the same license plate
    matches = LostVehicle.objects.filter(
        license_plate=found_vehicle.license_plate,
        status='searching'
    )
    
    for lost_vehicle in matches:
        # Create a match record
        match = VehicleMatch.objects.create(
            found_vehicle=found_vehicle,
            lost_vehicle=lost_vehicle
        )
        
        # Update statuses
        found_vehicle.status = 'matched'
        found_vehicle.save()
        
        lost_vehicle.status = 'found'
        lost_vehicle.save()
        
        # Send email notification
        send_match_notification(match)

def check_for_matches_with_lost(lost_vehicle):
    """Check if a lost vehicle matches any found vehicles"""
    # Look for found vehicles with the same license plate
    matches = FoundVehicle.objects.filter(
        license_plate=lost_vehicle.license_plate,
        status='pending'
    )
    
    for found_vehicle in matches:
        # Create a match record
        match = VehicleMatch.objects.create(
            found_vehicle=found_vehicle,
            lost_vehicle=lost_vehicle
        )
        
        # Update statuses
        found_vehicle.status = 'matched'
        found_vehicle.save()
        
        lost_vehicle.status = 'found'
        lost_vehicle.save()
        
        # Send email notification
        send_match_notification(match)

def send_match_notification(match):
    """Send email notification to the vehicle owner"""
    subject = 'Your Vehicle Has Been Found!'
    
    # Create email content
    html_message = render_to_string('vehicles/email/match_notification.html', {
        'match': match,
        'found_vehicle': match.found_vehicle,
        'lost_vehicle': match.lost_vehicle,
    })
    
    # Send email
    send_mail(
        subject=subject,
        message=f"Your vehicle ({match.lost_vehicle.make} {match.lost_vehicle.model}) has been found at {match.found_vehicle.location}!",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[match.lost_vehicle.owner_email],
        html_message=html_message,
        fail_silently=False,
    )
    
    # Update notification status
    match.notification_sent = True
    match.save()

def check_matches(request):
    """API endpoint to manually check for matches"""
    if request.method == 'POST':
        # Check all pending found vehicles against all searching lost vehicles
        found_vehicles = FoundVehicle.objects.filter(status='pending')
        matches_count = 0
        
        for vehicle in found_vehicles:
            # Look for lost vehicles with the same license plate
            matches = LostVehicle.objects.filter(
                license_plate=vehicle.license_plate,
                status='searching'
            )
            
            for lost_vehicle in matches:
                # Create a match record
                match = VehicleMatch.objects.create(
                    found_vehicle=vehicle,
                    lost_vehicle=lost_vehicle
                )
                
                # Update statuses
                vehicle.status = 'matched'
                vehicle.save()
                
                lost_vehicle.status = 'found'
                lost_vehicle.save()
                
                # Send email notification
                send_match_notification(match)
                
                matches_count += 1
        
        return JsonResponse({
            'success': True,
            'matches': matches_count,
            'message': f'Found {matches_count} new matches'
        })
    
    return JsonResponse({'success': False, 'message': 'Method not allowed'}, status=405)
