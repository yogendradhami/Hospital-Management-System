from django.shortcuts import render,redirect, HttpResponse
# from django.contrib.auth.models import User
from .models import AddMedicine,AddDoctor,Doctor,Department,BookAppointment, Contactus,Footer,Drug,Patient, Pharmacy,Staff,Services
from .forms import  AddDoctorCreateForm,BookAppointmentCreateForm,DrugCreateForm, patientCreateForm,staffCreateForm
from django.contrib import messages
import datetime

from django.views import View
# from django.views.generic.edit import FormView

# this is for search
from app_hospital_system.models import Doctor, Department, AddDoctor,BookAppointment, Contactus,Footer,Drug,Patient,Pharmacy

# for authentication 
from django.contrib.auth.decorators import login_required

# paginator
from django.core.paginator import Paginator

# Create your views here.
@login_required(login_url= 'user_login')
def Home(request):
    return render(request, 'layouts/master.html')


# def logintem(request):
#     if request.method == 'POST':
#         inote = request.POST['inote']
#         first_name= request.POST['first_name']
#         add_medicine= AddMedicine(first_name=first_name,inote=inote)
#         add_medicine.save()
#     return render(request, 'logintemp.html')


# this funtions shows the department page

@login_required(login_url= 'user_login')
def Department_Index(request):
    return render(request, 'department/department_index.html')




# this is to add the doctor in appointment  page
@login_required(login_url= 'user_login')
def Add_Doctor(request):
    data= AddDoctor()
    department=Department.objects.all()
    doc_create_form =  AddDoctorCreateForm()

    # method two with FormCLass object posting of images
    # doc_data=AddDoctorCreateForm(request.POST,request.FILES)
    # if doc_data.is_valid():
    #     doc_data.save()
    
    context={"form": doc_create_form, "data":data, "department": department}

    if request.method == "POST":
        doc=AddDoctor()
        department=  Department.objects.get(id=request.POST.get('department'))
        doc.name= request.POST.get('name')
        doc.specialization= request.POST.get('specialization')
        doc.department = department
        doc.image= request.FILES.get('image')
        doc.save()

        messages.success(request, 'Docotor added successfully')
        return redirect('book-appointment')

    return render(request,'book_appointment/add_doctor.html',context)

# This is for the BookAppointment index page
@login_required(login_url= 'user_login')
def Appointment_Index(request):
    posts=AddDoctor.objects.all()
    context={'posts':posts}
    return render(request, 'book_appointment/appointment_index.html',context)


# this is for booking the appointment
@login_required(login_url= 'user_login')
def Book_Appointment(request):

    data = BookAppointment()
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
        return redirect('book-appointment')
    
    return render(request, 'book_appointment/book_appointment.html',context)

# this displays the contactus page
@login_required(login_url= 'user_login')
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


# this class for the footer page
class Footer_Page(View):
    def get(self,request):
        return render(request, 'component/footer.html')
    

    def post(self, request):

        if request.method== 'POST':
            name= request.POST['name']
            email = request.POST['email']
            context= Footer(name= name, email=email)
            context.save()

            messages.success(request, "You're suscribed")
            return redirect('footer')
        

# functions for staff stats here
@login_required(login_url= 'user_login')
def Staff_Index(request):
    data = Staff.objects.all()
    context={
        'data':data
    }
  
    return render(request, 'staff/staf/index_staff.html',context )

@login_required(login_url= 'user_login')
def Staff_Add(request):
    data= Staff()
    context= {'form':data}

    if request.method=='POST':
        stf=Staff()
        stf.name = request.POST.get('name')
        stf.address= request.POST.get('address')
        stf.contact = request.POST.get('contact')
        stf.gender = request.POST.get('gender')
        stf.designation = request.POST.get('designation')
        stf.duty_time = request.POST.get('duty_time')
        stf.duty_ward = request.POST.get('duty_ward')
        stf.image=request.FILES.get('image')
        stf.save()

        messages.success(request, 'Staff added successfully in table')
        return redirect('staff-index')

    return render(request, 'staff/staf/add_staff.html',context)

@login_required(login_url= 'user_login')
def Staff_View(request,id):
    data=Staff.objects.get(id=id)
    context= {'data':data}
    return render(request, 'staff/staf/view_staff.html',context)


@login_required(login_url= 'user_login')
def Staff_Edit(request,id):
    data= Staff.objects.get(id=id)
    context= {
        'data':data
    }
    return render(request, 'staff/staf/edit_staff.html',context)


@login_required(login_url= 'user_login')
def Staff_Update(request):
    if request.method== 'POST':
        stf=Staff.objects.get(id=request.POST.get('id'))
        stf.name=request.POST.get('name')
        stf.address = request.POST.get('address')
        stf.contact = request.POST.get('contact')
        stf.gender = request.POST.get('gender')
        stf.designation = request.POST.get('designation')
        stf.duty_time = request.POST.get('duty_time')
        stf.duty_ward = request.POST.get('duty_ward')
        stf.image = request.POST.get('image')
        stf.save()
        messages.success(request, "Staff Edited Successfully")
        return redirect('staff-index')


@login_required(login_url= 'user_login')
def Staff_Delete(request,id):
    data=Staff.objects.get(id=id)
    data.delete()
    messages.success(request,'Staff Details deleted successfully!!')
    return redirect('staff-index')

# function for staff ends here


# function for  Drug starts here

@login_required(login_url= 'user_login')
def Drug_Index(request):
    drug_list= Drug.objects.all()
    pharm = Pharmacy.objects.all()
    context= {"data":pharm}
    context ={'data':drug_list, "dat":pharm}
    return render(request, 'drug/index_drug.html',context)


@login_required(login_url= 'user_login')
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

# function for drug ends here

# funtion for patient page starts here 
@login_required(login_url= 'user_login')
def Patient_Index(request):
    patient_list = Patient.objects.all()
    context={"data":patient_list}

    return render(request, 'staff/patient/index_patient.html',context)


@login_required(login_url= 'user_login')
def Patient_view(request,id):
    data= Patient.objects.get(id=id)
    context= {"data":data}
    return render(request, 'staff/patient/view_patient.html',context)


@login_required(login_url= 'user_login')
def Patient_Add(request):
    # patinet_create_form = patientCreateForm()
    data = Patient()
    # context= {"form":patinet_create_form}
    context={"data":data}

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


@login_required(login_url= 'user_login')
def Patient_delete(request,id):
    data = Patient.objects.get(id=id)
    data.delete()
    messages.success(request,'Patient Details deleted successfully!!')
    return redirect('patient-index')


@login_required(login_url= 'user_login')
def Patient_edit(request,id):
    data = Patient.objects.get(id=id)
    context= {"data":data}
    return render(request, 'staff/patient/edit_patient.html',context)


@login_required(login_url= 'user_login')
def Patient_update(request):
     if request.method == "POST":
        pnt=Patient.objects.get(id=request.POST.get('id'))
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

        messages.success(request, "Patient Edited Successfully")
        return redirect('patient-index')
    
# funtion for patients ends here

# funtion for pharmacy starts here

@login_required(login_url= 'user_login')
def Index_pharmacy(request):
    pharm = Pharmacy.objects.all()
    context= {"data":pharm}

    if request.method ==  "POST":
        phar= Pharmacy()
        phar.generic_name = request.POST.get('generic_name')
        phar.medicine_name= request.POST.get('medicine_name')
        phar.save()

        messages.success(request, "Medicine Added Successfully !!!")
        return redirect('pharmacy-index')


    return render(request, 'department/pharmacy_management_system/index_pharmacy.html',context)


@login_required(login_url= 'user_login')
def Pharmacy_delete(request,id):
    data = Pharmacy.objects.get(id=id)
    data.delete()
    messages.success(request,'Medicine Detail deleted successfully!!')
    return redirect('pharmacy-index')

# funtion for pharmcy ends here

# this shows the index service functoin
@login_required(login_url= 'user_login')
def Index_Service(request):
    ServiceData = Services.objects.all()

    # logic for search
    if request.method == 'GET':
        st=request.GET.get('query')
        if st!=None:
            ServiceData=Services.objects.filter(title__icontains=st)

    # this code for pagination
    paginator= Paginator(ServiceData,2)
    page_number = request.GET.get('page')
    ServiceDataFinal= paginator.get_page(page_number)
    totalpage=ServiceDataFinal.paginator.num_pages

    


    data = {
        
        "post":ServiceDataFinal,
        "lastpage": totalpage,
        "totalPageList":[n+1 for n in range(totalpage)]
    }

    return render(request, 'department/services/index_service.html',data)



# this is for showing doctor index
@login_required(login_url= 'user_login')
def Doctor_index(request):
   
    posts = Doctor.objects.all()
    context= {'posts':posts}


    return render(request, 'staff/doctor/index_doctor.html',context)


# this function for search 
@login_required(login_url= 'user_login')
def Search(request):
    query = request.GET['query']
    if len(query)>80:
        allPosts= [] # get.objects.none()
    else:
        allPostsTitle = Doctor.objects.filter(title__icontains=query)
        allPostsDoctorName = Doctor.objects.filter(doctor_name__icontains=query)
        allPosts= allPostsTitle.union(allPostsDoctorName)

        allPostsDepName = Department.objects.filter(department_name__icontains=query)
        allPostsDepSname = Department.objects.filter(department_name__icontains=query)
        allPosts= allPostsDepName.union(allPostsDepSname)

        allPostsPhar = Pharmacy.objects.filter(generic_name__icontains=query)
        allPostsPharM = Pharmacy.objects.filter(medicine_name__icontains=query)
        allPosts= allPostsPhar.union(allPostsPharM)

        patient= Patient.objects.filter(patient_name__icontains=query)
        allPosts = patient

        drug= Drug.objects.filter(name__icontains=query)
        allPosts = drug

        footer= Footer.objects.filter(name__icontains=query)
        allPosts = footer

        contact_us= Contactus.objects.filter(name__icontains=query)
        allPosts = contact_us

        book_appointment= BookAppointment.objects.filter(full_name__icontains=query)
        allPosts = book_appointment

        add_doctor= AddDoctor.objects.filter(name__icontains=query)
        allPosts = add_doctor


    if allPosts.count == 0:
        messages.warning(request, "No search result found. Please refine your query.")
    params = {'allPosts':allPosts,
               'query':query
            }
    return render(request, 'component/search.html',params)
