from django import forms
from .models import AddMedicine, AddDoctor,BookAppointment,  Drug

class AddMedicineCreateForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = AddMedicine

class AddDoctorCreateForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = AddDoctor
        

class BookAppointmentCreateForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = BookAppointment

class DrugCreateForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Drug