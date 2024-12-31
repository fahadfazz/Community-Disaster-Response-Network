# cdrn_app_new/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page URL
    path('report-incident/', views.report_incident, name='report_incident'),
    path('donate-resource/', views.donate_resource, name='donate_resource'),
    path('register-volunteer/', views.register_volunteer, name='register_volunteer'),
    path('donate-blood/', views.donate_blood, name='donate_blood'),
    path('incidents/', views.incident_list, name='incident_list'),
    path('resources/', views.resource_list, name='resource_list'),
    path('volunteers/', views.volunteer_list, name='volunteer_list'),
    path('blood-donations/', views.blood_donation_list, name='blood_donation_list'),
]

