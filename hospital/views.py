from rest_framework import viewsets

from mysite.hospital.models import Doctor, Appointment, Result, Feedback, PatientProfile
from mysite.hospital.serializers import DoctorSerializer, AppointmentSerializer, ResultSerializer, FeedbackSerializer, \
    PatientProfileSerializer


class PatientProfileViewSet(viewsets.ModelViewSet):
    queryset = PatientProfile.objects.all()
    serializer_class = PatientProfileSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    ordering_fields = ['price']
    search_fields = ['specialty', 'department__name']


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

