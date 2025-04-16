from django.db import models
from django.utils import timezone

class BaseVehicle(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    license_plate = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='vehicles/', null=True, blank=True)
    reported_date = models.DateTimeField(default=timezone.now)
    
    class Meta:
        abstract = True

class FoundVehicle(BaseVehicle):
    location = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    landmark = models.CharField(max_length=255, blank=True, null=True)
    condition = models.TextField()
    notes = models.TextField(blank=True, null=True)
    reporter_name = models.CharField(max_length=100, blank=True, null=True)
    reporter_email = models.EmailField(blank=True, null=True)
    status = models.CharField(max_length=20, default='pending', 
                             choices=[('pending', 'Pending'), ('matched', 'Matched')])
    
    def __str__(self):
        return f"{self.color} {self.make} {self.model} - {self.license_plate}"

class LostVehicle(BaseVehicle):
    last_seen_location = models.CharField(max_length=255)
    last_seen_date = models.DateField()
    last_seen_time = models.TimeField(null=True, blank=True)
    circumstances = models.TextField(blank=True, null=True)
    features = models.TextField(blank=True, null=True)
    owner_name = models.CharField(max_length=100)
    owner_email = models.EmailField()
    owner_phone = models.CharField(max_length=20)
    alt_contact = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20, default='searching', 
                             choices=[('searching', 'Searching'), ('found', 'Found')])
    
    def __str__(self):
        return f"{self.color} {self.make} {self.model} - {self.license_plate}"

class VehicleMatch(models.Model):
    found_vehicle = models.ForeignKey(FoundVehicle, on_delete=models.CASCADE)
    lost_vehicle = models.ForeignKey(LostVehicle, on_delete=models.CASCADE)
    match_date = models.DateTimeField(default=timezone.now)
    notification_sent = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Match: {self.lost_vehicle.license_plate}"
