from django.contrib import admin
from.models import AddMedicine, AddDoctor, BookAppointment, Department, Doctor,Contactus,Footer,Drug, Patient,Pharmacy,Staff

# Register your models here.

# to style the admin panel
# class AdminBookAppointment(admin.ModelAdmin):
#     list_display= ('full_name','contact','email')


admin.site.register(AddMedicine)
admin.site.register(AddDoctor)
admin.site.register(BookAppointment)
admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(Contactus)
admin.site.register(Footer)
admin.site.register(Drug)
admin.site.register(Patient)
admin.site.register(Pharmacy)
admin.site.register(Staff)



# to rename the admin panel records

admin.site.site_header= "HMS"
admin.site.site_title= 'HMS'
admin.site.index_title= 'Admin_panel'