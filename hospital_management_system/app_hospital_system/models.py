from django.db import models

# Create your models here.
class AddMedicine(models.Model):
    first_name =models.CharField(max_length=200)
    inote = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name



# department model
class Department(models.Model):
    department_name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=255, null=True, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.short_name

    class Meta:
        db_table = "app_department"

class AddDoctor(models.Model):
    name= models.CharField(max_length=100)
    specialization = models.CharField(max_length=200,null=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='static/img/doctor/')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "app_adddoctor"
  
  


# Doctors model for doctor details
class Doctor(models.Model):
    title= models.CharField(max_length=200)
    doctor_name = models.CharField(max_length=255)
    doctor_address=models.CharField(max_length=100)
    doctor_number= models.CharField(max_length=50)
    doctor_gender = models.CharField(max_length=50)
    doctor_specialization= models.CharField(max_length=150)
    # short_name = models.CharField(max_length=255, null=True, blank=True)
    status = models.BooleanField(default=True)
    message=models.TextField()

    def __str__(self):
        return self.doctor_name

    class Meta:
        db_table = "app_doctor"

        
# model for booking appointment
class BookAppointment(models.Model):
    full_name = models.CharField(max_length=255) 
    contact = models.CharField(max_length=255)
    email = models.EmailField()
    appointment_date =  models.DateField()
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    select_doctor=models.ForeignKey(AddDoctor, on_delete=models.CASCADE)
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = "app_bookappointment"   


# model for contactus
class Contactus(models.Model):
    name = models.CharField(max_length=100)
    email =models.EmailField()
    subject= models.CharField(max_length=500)
    message = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = "app_contactus"
    

# model for footer subscription
class Footer(models.Model):
    name=models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name
    class Meta:
        db_table = "app_footer"
    

class Drug(models.Model):
    name = models.CharField(max_length=299)
    
    specification =  models.TextField()
   
    cost = models.CharField(max_length=100)
    availability = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        db_table = "app_drug"


# Patient model

class Patient(models.Model):
    patient_name = models.CharField(max_length=100)
    patient_contact = models.CharField(max_length=100)
    patient_address = models.CharField(max_length=100)
    patients_doctor = models.CharField(max_length=100)
    patient_admit_date = models.DateField()
    patient_release_date= models.DateField()
    patient_days_spent= models.CharField(max_length=199)

    patient_age = models.CharField(max_length=100)
    patient_last_visit =  models.CharField(max_length=100)
    patient_status=  models.CharField(max_length=100)
    patient_disease_symptoms= models.CharField(max_length=100,null=True)

    def __str__(self):
        return  self.patient_name
    class Meta:
        db_table = "app_patient"

class Pharmacy(models.Model):
    generic_name= models.CharField(max_length=100)
    medicine_name= models.CharField(max_length=100)

    def __str__(self):
        return self.generic_name
    
    class Meta:
        db_table = "app_pharmacy"

class Staff(models.Model):
    name = models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    designation =models.CharField(max_length=100)
    duty_time=models.CharField(max_length=100)
   
    duty_ward=models.CharField(max_length=100)
    image=models.ImageField(upload_to='static/img/staff')
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "app_staff"
