from django import forms
from .models import FoundVehicle, LostVehicle

class FoundVehicleForm(forms.ModelForm):
    class Meta:
        model = FoundVehicle
        fields = ['make', 'model', 'color', 'license_plate', 'photo', 
                  'location', 'city', 'state', 'zipcode', 'landmark', 
                  'condition', 'notes', 'reporter_name', 'reporter_email']
        widgets = {
            'condition': forms.Textarea(attrs={'rows': 3}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }

class LostVehicleForm(forms.ModelForm):
    class Meta:
        model = LostVehicle
        fields = ['make', 'model', 'year', 'color', 'license_plate', 'vin_number', 
                  'engine_number', 'photo', 'last_seen_location', 'last_seen_date', 
                  'last_seen_time', 'circumstances', 'features', 'owner_name', 
                  'owner_email', 'owner_phone', 'alt_contact']
        widgets = {
            'last_seen_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'last_seen_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'circumstances': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'features': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'make': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Toyota, Ford, Honda'}),
            'model': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Camry, F-150, Civic'}),
            'year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 2020'}),
            'color': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Red, Blue, Black'}),
            'license_plate': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter full license plate number'}),
            'vin_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter VIN or Chassis Number'}),
            'engine_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter engine number if available'}),
            'last_seen_location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address or area where vehicle was last seen'}),
            'owner_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your full name'}),
            'owner_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your email address'}),
            'owner_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your phone number'}),
            'alt_contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Alternative contact method'}),
        }
