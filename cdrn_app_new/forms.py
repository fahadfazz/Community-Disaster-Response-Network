# cdrn_app_new/forms.py
from django import forms
from .models import Incident, Resource, Volunteer, BloodDonation

class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['name', 'description', 'location', 'status', 'image']

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['name', 'description', 'quantity', 'available', 'incident']

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['name', 'phone_number', 'email', 'skills', 'available_for']

class BloodDonationForm(forms.ModelForm):
    class Meta:
        model = BloodDonation
        fields = ['donor_name', 'blood_type', 'quantity']
