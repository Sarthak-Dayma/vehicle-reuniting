from django.contrib import admin
from .models import FoundVehicle, LostVehicle, VehicleMatch

@admin.register(FoundVehicle)
class FoundVehicleAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'color', 'license_plate', 'location', 'reported_date', 'status')
    list_filter = ('status', 'make', 'color')
    search_fields = ('make', 'model', 'license_plate', 'location')
    date_hierarchy = 'reported_date'

@admin.register(LostVehicle)
class LostVehicleAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'color', 'license_plate', 'last_seen_location', 'owner_name', 'status')
    list_filter = ('status', 'make', 'color')
    search_fields = ('make', 'model', 'license_plate', 'owner_name', 'owner_email')
    date_hierarchy = 'reported_date'

@admin.register(VehicleMatch)
class VehicleMatchAdmin(admin.ModelAdmin):
    list_display = ('found_vehicle', 'lost_vehicle', 'match_date', 'notification_sent')
    list_filter = ('notification_sent',)
    date_hierarchy = 'match_date'
