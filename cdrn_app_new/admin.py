from django.contrib import admin
from .models import Incident, Resource, Volunteer, BloodDonation

# Register the Incident model with custom admin configuration
@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'location', 'date_reported', 'status')
    search_fields = ('name', 'description', 'location')
    list_filter = ('status', 'date_reported')
    ordering = ('-date_reported',)  # Order incidents by the most recent

# Register the Resource model with custom admin configuration
@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'quantity', 'available', 'incident')
    search_fields = ('name', 'description')
    list_filter = ('available', 'incident')
    ordering = ('name',)

# Register the Volunteer model with custom admin configuration
@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'skills', 'available_for', 'registered_at')
    search_fields = ('name', 'email', 'phone_number')
    list_filter = ('available_for', 'registered_at')
    ordering = ('-registered_at',)

# Register the BloodDonation model with custom admin configuration
@admin.register(BloodDonation)
class BloodDonationAdmin(admin.ModelAdmin):
    list_display = ('donor_name', 'blood_type', 'quantity', 'donation_date')
    search_fields = ('donor_name', 'blood_type')
    list_filter = ('blood_type', 'donation_date')
    ordering = ('-donation_date',)
