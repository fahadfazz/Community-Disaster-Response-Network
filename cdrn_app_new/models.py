# cdrn_app_new/models.py
from django.db import models
from django.utils.timezone import now


class Incident(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    date_reported = models.DateTimeField(auto_now_add=True)
    status_choices = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='Pending')
 # Add image field for uploading photos (optional)
    image = models.ImageField(upload_to='incidents/', blank=True, null=True)



    def __str__(self):
        return self.name

class Resource(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    quantity = models.IntegerField()
    available = models.BooleanField(default=True)
    incident = models.ForeignKey(Incident, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class Volunteer(models.Model):
    AVAILABILITY_CHOICES = [
        ('General', 'General'),
        ('Disaster Relief', 'Disaster Relief'),
        ('Medical Aid', 'Medical Aid'),
        ('Food Distribution', 'Food Distribution'),
        ('Shelter Assistance', 'Shelter Assistance'),
        ('Logistics Support', 'Logistics Support'),
        ('Other', 'Other')
    ]
    
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15, default='000-000-0000', blank=True)
    email = models.EmailField(blank=True)
    skills = models.TextField(blank=True)
    available_for = models.CharField(max_length=100, choices=AVAILABILITY_CHOICES, default='General')
    registered_at = models.DateTimeField(default=now, auto_now_add=False)

    def __str__(self):
        return self.name

    def __str__(self):
        return self.name

class BloodDonation(models.Model):
    DONATION_STATUS_CHOICES = [
        ('Completed', 'Completed'),
        ('Pending', 'Pending'),
        ('Rejected', 'Rejected'),
    ]

    BLOOD_TYPE_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('Unknown', 'Unknown'),  # In case the blood type is unknown
    ]

    donor_name = models.CharField(max_length=200)
    blood_type = models.CharField(max_length=10, choices=BLOOD_TYPE_CHOICES)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)  # Quantity in liters or units
    donation_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=DONATION_STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.donor_name} - {self.blood_type} - {self.status}"