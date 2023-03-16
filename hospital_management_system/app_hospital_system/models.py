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
    specializaion = models.CharField(max_length=200)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "app_adddoctor"
  
  


# Doctors model
class Doctor(models.Model):
    doctor_name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=255, null=True, blank=True)
    status = models.BooleanField(default=True)
    message=models.CharField(max_length=100)

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
    