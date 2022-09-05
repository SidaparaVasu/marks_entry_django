from django import forms  
from auth_app.models import users
 
class RegisterForm(forms.ModelForm):  
    class Meta:  
        model = users  
        fields = ('username','email','phoneno','password',) 