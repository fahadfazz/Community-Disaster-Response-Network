# cdrn_app_new/views.py
from django.shortcuts import render, redirect
from .models import Incident, Resource, Volunteer, BloodDonation
from .forms import IncidentForm, ResourceForm, VolunteerForm, BloodDonationForm

def home(request):
    return render(request, 'home.html')

def report_incident(request):
    if request.method == 'POST':
        form = IncidentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('incident_list')
    else:
        form = IncidentForm()
    return render(request, 'report_incident.html', {'form': form})

def donate_resource(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resource_list')
    else:
        form = ResourceForm()
    return render(request, 'donate_resource.html', {'form': form})

def register_volunteer(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('volunteer_list')
    else:
        form = VolunteerForm()
    return render(request, 'register_volunteer.html', {'form': form})

def donate_blood(request):
    if request.method == 'POST':
        form = BloodDonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blood_donation_list')
    else:
        form = BloodDonationForm()
    return render(request, 'donate_blood.html', {'form': form})

def incident_list(request):
    incidents = Incident.objects.all()
    return render(request, 'incident_list.html', {'incidents': incidents})

def resource_list(request):
    resources = Resource.objects.all()
    return render(request, 'resource_list.html', {'resources': resources})

def volunteer_list(request):
    volunteers = Volunteer.objects.all()
    return render(request, 'volunteer_list.html', {'volunteers': volunteers})

def blood_donation_list(request):
    donations = BloodDonation.objects.all()
    return render(request, 'blood_donation_list.html', {'donations': donations})
