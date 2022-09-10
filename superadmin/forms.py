from django import forms  
from superadmin.models import Institute, Course
 
class InstituteForm(forms.ModelForm):  
    class Meta:  
        model = Institute  
        fields = ('instituteID','instituteName','instituteAddress',)

class CourseForm(forms.ModelForm):  
    class Meta:  
        model = Course  
        fields = ('courseID','courseName','instituteID',)