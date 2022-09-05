from django import forms  
from superadmin.models import addInstitute
 
class AddInstitute(forms.ModelForm):  
    class Meta:  
        model = addInstitute  
        fields = ('instituteId','instituteName','instituteAddress',)
        