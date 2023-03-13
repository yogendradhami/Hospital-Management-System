from django.shortcuts import render,redirect
# from django.contrib.auth.models import User
from .models import AddMedicine,AddDoctor,Doctor,Department,BookAppointment
from .forms import AddMedicineCreateForm, AddDoctorCreateForm,BookAppointmentCreateForm
from django.contrib import messages



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

def AppointmentIndex(request):
    return render(request, 'book_appointment/appointment_index.html')


def AddDoctor(request):
    doc_create_form = AddDoctorCreateForm()
    context = {'form':doc_create_form}

    if request.method == 'POST':
        doc = AddDoctor()
        doc.name = request.POST.get('name')
        doc.specialization = request.POST.get('specialization')
        doc.save()

        messages.success(request, 'Doctor Added Successfully!!')

        return redirect('book-appointment')
    return render(request,'book_appointment/add_doctor.html', context)

def MakeOrder(request):
    return render(request, 'book_appointment/order.html')

def BookAppointment(request):
    data= BookAppointment.objects.get()
    department = Department.objects.all()
    doctor= Doctor.objects.all()
    context= {"data":data, "department":department, "doctor":doctor}

    if request.method == 'POST':
        book_app = BookAppointment()
        doctor = Doctor.objects.get(id=request.POST.get('doctor'))
        department = Department.objects.get(id=request.POST.get('department'))
        book_app.full_name = request.post.get('full_name')
        book_app.contact=request.POST.get('contact')
        book_app.email=request.POST.get('email')
        book_app.appointment_date=request.POST.get('appointment_date')
        book_app.message=request.POST.get('message')
        book_app.doctor= doctor
        book_app.department = department
        book_app.save()
        
        messages.success(request, "You're appointment has been booked with Dr.{{ doctor_name }}")
        return  redirect('book-appointment')


    return render(request, 'book_appointment/book_appointment.html',context)