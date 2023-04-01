from django.shortcuts import render
from .serializers import BookappointmentSerializer
from app_hospital_system.models import BookAppointment,Department


from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework.views import APIView


# Create your views here.
class CustomResponse():
    def successResponse(self, code,   msg,  data=dict()):
        context={
            "status_code":code,
            "message":msg,
            "data":data,
            "error":[]
        }
        return context
    

class BookappointmetApiView(APIView):
    def get(self, request):
        bookappointment= BookAppointment.objects.all()
        serializer= BookappointmentSerializer(bookappointment, many=True)
       
        return Response(CustomResponse.successResponse(200, "Doctors Lists", serializer.data), status=status.HTTP_200_OK)
    
    def post(self, request):
        # data={
        # "full_name": request.POST.get('full_name'),
        # "contact": request.POST.get('contact'),
        # "email": request.POST.get('email'),
        # "appointment_date": request.POST.get('appointment_date'),
        # "message": request.POST.get('message'),
        # "department": request.POST.get('department'),
        # "select_doctor": request.POST.get('select_doctor'),
        # "department": request.POST.get('department'),

        # }
        serializer= BookappointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(CustomResponse.successResponse(200, "Added successfully", serializer.data))
        return Response(serializer.errors, status=status.HTTP_408_BAD_REQUEST_TIMEOUT)

class BookappointmentApiIdView(APIView):
    def get(self,request, id):
        pass
    
    def put(self,request, id):
        pass
    
    def delete(self, request, id):
        pass

