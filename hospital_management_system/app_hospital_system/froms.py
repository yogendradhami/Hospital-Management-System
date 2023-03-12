from django import forms
from .models import AddMedicine

class AddMedicineCreateForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = AddMedicine