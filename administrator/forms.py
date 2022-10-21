from django import forms  
from django.views.generic import ListView
from .models import Batch,Semester,Subject,Student
 
class BatchForm(forms.ModelForm):  
    class Meta:  
        model = Batch  
        fields = ('batchName','courseName') 

class SemesterForm(forms.ModelForm, ListView):  
    class Meta:  
        paginate_by = 10
        model = Semester  
        fields = ('semester','courseName') 

class SubjectForm(forms.ModelForm):  
    class Meta:  
        model = Subject  
        fields = ('courseName','subject','semester','credits') 


class StudentForm(forms.ModelForm):  
    class Meta:  
        model = Student  
        fields = (
            'instituteName','courseName','semester','batchName',
            'enrolment','seatno','name', 'email', 'phoneno', 'gender', 'category'
        ) 