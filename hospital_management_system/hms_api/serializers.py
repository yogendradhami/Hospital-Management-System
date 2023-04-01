from rest_framework import serializers
from app_hospital_system.models import BookAppointment

class BookappointmentSerializer(serializers.ModelSerializer):
    class  Meta:
        model = BookAppointment
        fields = "__all__"