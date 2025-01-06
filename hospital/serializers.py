from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'email', 'role', 'phone_number', 'profile_picture']


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'description']


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('user', 'specialty','working_days','shift_start','shift_end','price','department')


class PrescriptionSerializer(serializers.ModelSerializer):
    doctor = serializers.StringRelatedField()
    patient = serializers.StringRelatedField()

    class Meta:
        model = Prescription
        fields = ['id', 'doctor', 'patient', 'medication', 'dosage', 'prescribed_at']


class PatientProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientProfile
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'


class WardSerializer(serializers.ModelSerializer):
    department = serializers.StringRelatedField()

    class Meta:
        model = Ward
        fields = ['id', 'name', 'department', 'capacity']