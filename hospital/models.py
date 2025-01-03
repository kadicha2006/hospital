from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.role

    groups = None
    user_permissions = None


class PatientProfile(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='patient_profile')
    emergency_contact = models.CharField(max_length=15, blank=True, null=True)
    blood_type = models.CharField(max_length=3, blank=True, null=True)
    allergies = models.TextField(blank=True, null=True)
    medical_history = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user


class Doctor(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='doctor_profile')
    specialty = models.CharField(max_length=100)
    shift_start = models.TimeField()
    shift_end = models.TimeField()
    working_days = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return self.user


class Appointment(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    status = models.CharField(max_length=10)


class Result(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    diagnosis = models.TextField()
    treatment = models.TextField()
    prescribed_medication = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Feedback(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
