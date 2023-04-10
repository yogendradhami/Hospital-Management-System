from django import forms
from .models import AddMedicine, AddDoctor,BookAppointment,Drug, Patient, Staff, Price

class AddMedicineCreateForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = AddMedicine

# for for AddDoctor page

class AddDoctorCreateForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = AddDoctor
        

# form for Bookappointmentpage

class BookAppointmentCreateForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = BookAppointment

# form for drug page
class DrugCreateForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Drug

# form for patient
class patientCreateForm(forms.ModelForm):
    class Meta:
        fields= '__all__'
        model = Patient

# form for staff

class staffCreateForm(forms.ModelForm):
    class Meta:
        fields= '__all__'
        model = Staff

class PriceCreateForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model= Price