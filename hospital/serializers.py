from rest_framework import serializers
from rest_framework.authtoken.admin import User

from mysite.hospital.models import Doctor, PatientProfile, Result, Appointment, Feedback


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'phone_number', 'profile_picture']


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


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