from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields = ('Fullname' , 'Mobile','emp_code' , 'Position')
        labels = {
            'Fullname' : 'Full Name',
            'emp_code' : 'EMP. Code'
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['Position'].empty_label = "Select"
        self.fields['emp_code'].required = False