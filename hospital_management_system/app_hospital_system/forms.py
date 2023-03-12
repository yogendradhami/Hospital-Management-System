from django import forms
from .models import AddMedicine, AddDoctor

class AddMedicineCreateForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = AddMedicine

class AddDoctorCreateForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = AddDoctor