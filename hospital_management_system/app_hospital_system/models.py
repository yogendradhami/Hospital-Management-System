from django.db import models

# Create your models here.
class AddMedicine(models.Model):
    first_name =models.CharField(max_length=200)
    inote = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name

class AddDoctor(models.Model):
    name= models.CharField(max_length=100)
    specializaion = models.CharField(max_length=200)

    def __str__(self):
        return self.name