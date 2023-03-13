from django.contrib import admin
from.models import AddMedicine, AddDoctor, BookAppointment, Department, Doctor
# Register your models here.
admin.site.register(AddMedicine)
admin.site.register(AddDoctor)
admin.site.register(BookAppointment)
admin.site.register(Department)
admin.site.register(Doctor)

