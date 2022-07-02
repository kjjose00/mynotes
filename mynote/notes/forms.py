
from email.mime import image
from django import forms

from .models import Notes
from django.contrib.auth.models import User
from .models import UserAccount
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class NotesForm(forms.ModelForm):
    class Meta:
        model=Notes
        fields=['note','image','user']
        widgets={'note':forms.Textarea(attrs={'rows':3,'placeholder':'Type your notes here...','class':'form-control'}),'image':forms.FileInput(attrs={'class':'form-control'}),'user':forms.HiddenInput()}
   

class SignUpForm(UserCreationForm):
    
  
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Password Confirm',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'Email'}
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),'first_name':forms.TextInput(attrs={'class':'form-control'}),'last_name':forms.TextInput(attrs={'class':'form-control'}),'email':forms.EmailInput(attrs={'class':'form-control'})}
        
    
class LoginForm(AuthenticationForm):
    class Meta:
        model=User
        fields=['username','password']
        widgets={'username':forms.TextInput(attrs={'class':'form-control','id':'form2Example1'}),'password':forms.PasswordInput(attrs={'class':'form-control','id':'form2Example2'})}
       
class SignupImageForm(forms.Form):
    image=forms.FileField(label='Upload your Image',required=False,widget=forms.FileInput(attrs={'class':'form-control my-3'}))

