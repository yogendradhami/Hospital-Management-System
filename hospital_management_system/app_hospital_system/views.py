from django.shortcuts import render,redirect
# from django.contrib.auth.models import User
from .models import AddMedicine,AddDoctor,Doctor,Department,BookAppointment, Contactus,Footer
from .forms import AddMedicineCreateForm, AddDoctorCreateForm,BookAppointmentCreateForm
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

def DepartmentIndex(request):
    return render(request, 'department/department_index.html')

def AppointmentIndex(request):
    return render(request, 'book_appointment/appointment_index.html')


def AddDoctor(request):
    doc_create_form = AddDoctorCreateForm()
    context={"form": doc_create_form}

    if request.method == "POST":
        doc=AddDoctor( )
        department=  Department.objects.get(id=request.POST.get('department'))
        doc.name= request.POST.get('name')
        doc.specialization= request.POST.get('specialization')
        doc.department = department

        doc.save()

        messages.success(request, 'Docotor added successfully')


    return render(request,'book_appointment/add_doctor.html',context)




def MakeOrder(request):
    return render(request, 'book_appointment/order.html')

def BookAppointment(request):
    if request.method=='POST':
        book = BookAppointment()
        department=  Department.objects.get(id=request.POST.get('department'))
        select_doctor=  AddDoctor.objects.get(id=request.POST.get('select_doctor'))

        book.name = request.POST.get('name')
        book.email=request.POST.get('email')
        book.number=request.POST.get('number')
        book.appointment_date=request.POST.get('appointment_date')
        book.department= department
        book.select_doctor=select_doctor
        book.message=request.POST.get('message')
        book.save()
    
        messages.success(request, 'Appointment Booked successfully')
    
    return render(request, 'book_appointment/book_appointment.html')



def ContactUs(request):
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


class FooterPage(View):
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
    
    


# def today(request):
#     """Shows todays current time and date."""
#     today = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
#     context = {'today': today}
#     return render(request, 'component/footer.html', context)