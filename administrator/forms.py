from django import forms  
from .models import Batch,Semester,Subject
 
class BatchForm(forms.ModelForm):  
    class Meta:  
        model = Batch  
        fields = ('batchName','courseName') 

class SemesterForm(forms.ModelForm):  
    class Meta:  
        model = Semester  
        fields = ('semester','courseName') 

class SubjectForm(forms.ModelForm):  
    class Meta:  
        model = Subject  
        fields = ('subject','semester','credits') 
