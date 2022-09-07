from django import forms  
from superadmin.models import Institute
 
class Institute(forms.ModelForm):  
    class Meta:  
        model = Institute  
        fields = ('instituteId','instituteName','instituteAddress',)
        