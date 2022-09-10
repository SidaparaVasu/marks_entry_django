from django import forms  
from superadmin.models import Institute
 
class InstituteForm(forms.ModelForm):  
    class Meta:  
        model = Institute  
        fields = ('instituteID','instituteName','instituteAddress',)
        