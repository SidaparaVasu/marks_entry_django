from django import forms  
from django.views.generic import ListView
from .models import Batch,Semester,Subject
 
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
        fields = ('subject','semester','credits') 
