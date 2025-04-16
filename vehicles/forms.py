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
        fields = ['make', 'model', 'color', 'license_plate', 'photo',
                  'last_seen_location', 'last_seen_date', 'last_seen_time',
                  'circumstances', 'features', 'owner_name', 'owner_email',
                  'owner_phone', 'alt_contact']
        widgets = {
            'last_seen_date': forms.DateInput(attrs={'type': 'date'}),
            'last_seen_time': forms.TimeInput(attrs={'type': 'time'}),
            'circumstances': forms.Textarea(attrs={'rows': 3}),
            'features': forms.Textarea(attrs={'rows': 3}),
        }
