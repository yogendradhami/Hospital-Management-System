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
    
    def errorResponse(self, code,   msg,  error=dict()):
        context={
            "status_code":code,
            "message":msg,
            "data":[],
            "error":error
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
        return Response(CustomResponse.errorResponse(408, "Validation Failed", serializer.errors))

class BookappointmentApiIdView(APIView):
    def get_object(self,request, id):
        try:
            data=BookAppointment.objects.all(id=id)
            return data
        except BookAppointment.DoesNotExist:
            return None

    def get(self, request, id):
        instance=self.get_object(id=id)

        if not instance:
            return Response({"msg":"Not Found"}, stats=status.HTTP_404_NOT_FOUND)
        
        serializer= BookappointmentSerializer(instance)
        return Response(serializer.data, status= status.HTTP_200_OK)

    def put(self,request, id):
        instance= self.get_object(id=id)
        if not instance:
            return Response({"msg":"Not Found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = BookappointmentSerializer(data=request, instance=instance)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.error,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        instance= self.get_object(id=id)

        if not instance:
            return Response({"msg":"Not Found"}, status=status.HTTP_404_NOT_FOUND)
        
        instance.delete()
        return Response({"msg":"Deleted succesfully"}, status=status.HTTP_200_OK)

