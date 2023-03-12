from django.shortcuts import render,redirect
# from django.contrib.auth.models import User
from .models import AddMedicine
from .froms import AddMedicineCreateForm


# Create your views here.


def Home(request):
    return render(request, 'layouts/master.html')


def logintem(request):
    if request.method == 'POST':
        inote = request.POST['inote']
        first_name= request.POST['first_name']
        add_medicine= AddMedicine(first_name=first_name,inote=inote)
        add_medicine.save()
    return render(request, 'logintemp.html')

def DepartmentIndex(request):
    return render(request, 'department/department_index.html')

def BookAppointment(request):
    return render(request, 'book_appointment/appointment_index.html')





