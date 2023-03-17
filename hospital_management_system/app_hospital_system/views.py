from django.shortcuts import render,redirect
# from django.contrib.auth.models import User
from .models import AddMedicine,AddDoctor,Doctor,Department,BookAppointment, Contactus,Footer,Drug,Patient
from .forms import AddMedicineCreateForm, AddDoctorCreateForm,BookAppointmentCreateForm,DrugCreateForm, patientCreateForm
from django.contrib import messages
import datetime
from django.views import View
# from django.views.generic.edit import FormView



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

def Department_Index(request):
    return render(request, 'department/department_index.html')

def Appointment_Index(request):
    posts=AddDoctor.objects.all()
    context={'posts':posts}
    return render(request, 'book_appointment/appointment_index.html',context)


def Add_Doctor(request):
    doc_create_form =  AddDoctorCreateForm()
    context={"form": doc_create_form}

    if request.method == "POST":
        doc=AddDoctor()
        department=  Department.objects.get(id=request.POST.get('department'))
        doc.name= request.POST.get('name')
        doc.specialization= request.POST.get('specialization')
        doc.department = department
        doc.image= request.POST.get('image')
        doc.save()

        messages.success(request, 'Docotor added successfully')
        return redirect('book-appointment')

    return render(request,'book_appointment/add_doctor.html',context)


def Book_Appointment(request):

    data = BookAppointment.objects.get()
    department=Department.objects.all()
    select_doctor= AddDoctor.objects.all()
    context = {"data":data, "department":department,"addDoctor":select_doctor}


    if request.method=='POST':
        book = BookAppointment()
        department=  Department.objects.get(id=request.POST.get('department'))
        select_doctor=  AddDoctor.objects.get(id=request.POST.get('select_doctor'))

        book.full_name = request.POST.get('full_name')
        book.email=request.POST.get('email')
        book.contact=request.POST.get('contact')
        book.appointment_date=request.POST.get('appointment_date')
        book.message=request.POST.get('message')

        book.department= department
        book.select_doctor=select_doctor
        book.save()
    
        messages.success(request, 'Appointment Booked successfully')
    
    return render(request, 'book_appointment/book_appointment.html',context)



def Contact_Us(request):
    context= {
        'Title':'Our Contact',
        'Location':'kathmandu',
        'Email':'hosital@org.com',
        'Call':'+01-02561455'
    }
    if request.method == 'POST':
       
        name = request.POST['name']
        email= request.POST['email']
        subject=request.POST['subject']
        message = request.POST['message']
        con= Contactus(name= name,email=email,subject=subject,message=message)
        con.save()

        messages.success(request, "You're request has been sent ")
        return redirect('contact-us')
    return render(request, 'book_appointment/contactus.html', context)


class Footer_Page(View):
    def get(self,request):
        return render(request, 'component/footer.html')
    

    def post(self, request):

        if request.method== 'POST':
            name= request.POST['name']
            email = request.POST['email']
            context= Footer(name= name, email=email)
            context.save()

            messages.success(request, "You're sucscribed")
            return redirect('footer')
        

def Staff_Index(request):
    
    
    return render(request, 'staff/index_staff.html', )

def Staff_Add(request):
    return render(request, 'staff/add_staff.html')

def Drug_Index(request):
    drug_list= Drug.objects.all()
    context ={'data':drug_list}
    return render(request, 'drug/index_drug.html',context)

def Drug_Add(request):
    drug_create_form = DrugCreateForm()
    context = {"form":drug_create_form}

    if request.method == "POST":
        drg = Drug()
        drg.name = request.POST.get('name')
        drg.specification= request.POST.get('specification')
        drg.cost= request.POST.get('cost')
        drg.availability= request.POST.get('availability')
        drg.save()

        messages.success(request, 'Drug added successfully in table')
        return redirect('drug-index')
    return render(request, 'drug/add_drug.html',context)


def Patient_Index(request):
    patient_list = Patient.objects.all()
    context={"data":patient_list}

    return render(request, 'staff/patient/index_patient.html',context)

def Patient_view(request):
    data= Patient.objects.get()
    context= {"data":data}
    return render(request, 'staff/patient/view_patient.html',context)

def Patient_Add(request):
    patinet_create_form = patientCreateForm()
    # data = Patient()
    context= {"form":patinet_create_form}


    if request.method == "POST":
        pnt=Patient()
        pnt.patient_name=request.POST.get('patient_name')
        pnt.patient_contact=request.POST.get('patient_contact')
        pnt.patient_address=request.POST.get('patient_address')
        pnt.patients_doctor=request.POST.get('patients_doctor')
        pnt.patient_admit_date=request.POST.get('patient_admit_date')
        pnt.patient_release_date=request.POST.get('patient_release_date')
        pnt.patient_days_spent=request.POST.get('patient_days_spent')
        pnt.patient_age=request.POST.get('patient_age')
        pnt.patient_last_visit=request.POST.get('patient_last_visit')
        pnt.patient_status=request.POST.get('patient_status')
        pnt.patient_disease_symptoms=request.POST.get('patient_disease_symptoms')
        pnt.save()

        messages.success(request, "Patient Added Successfully")
        return redirect('patient-index')
    return render(request, 'staff/patient/add_patient.html',context)

def Index_pharmacy(request):
    return render(request, 'department/pharmacy_management_system/index_pharmacy.html')

def Index_Service(request):
    return render(request, 'department/services/index_service.html')

def Doctor_index(request):
   
    posts = Doctor.objects.get()
    context= {'posts':posts}


    return render(request, 'staff/doctor/index_doctor.html',context)