from django.shortcuts import render
from .serializers import BookappointmentSerializer
from app_hospital_system.models import BookAppointment


from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework.views import APIView


# Create your views here.
class BookappointmetApiView(APIView):
    def get(self, request):
        bookappointment= BookAppointment.objects.all()
        serializer= BookappointmentSerializer(bookappointment, many=True)
        context={
            "status_code":200,
            "message":"Doctor Lists",
            "data":serializer.data,
            "error":[]
        }
        return Response(context, status=status.HTTP_200_OK)
    


    def post(self, request):
        pass

class BookappointmentApiIdView(APIView):
    def get(self,request, id):
        pass
    
    def put(self,request, id):
        pass
    
    def delete(self, request, id):
        pass

