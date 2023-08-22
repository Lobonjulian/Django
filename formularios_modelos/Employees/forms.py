from django.forms import ModelForm
from .models import Employee

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee 
        fields = ['name', 'last_name', 'email']
        

