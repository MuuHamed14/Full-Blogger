from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from .models import Profile

class SignUpForm(UserCreationForm):
    username = forms.CharField(label='الاسم',max_length=100,help_text='اسم المستخدم يجب ألا يحتوي على مسافات.')
    email = forms.CharField(label='البريد الالكتروني',max_length=100,widget=forms.EmailInput())
    first_name = forms.CharField(label='الاسم الاول')
    last_name = forms.CharField(label='الاسم الاخير')
    password1 = forms.CharField(label='كلمة المرور',min_length=8,widget=forms.PasswordInput())
    password2 = forms.CharField(label='تأكيد كلمة المرور',min_length=8,widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']

class LoginForm(forms.ModelForm):
     username = forms.CharField(label='الاسم',max_length=100)
     password = forms.CharField(label='كلمة المرور',min_length=8,widget=forms.PasswordInput())

     class Meta:
        model = User
        fields = ['username','password']

class User_Update(forms.ModelForm):
    first_name = forms.CharField(label='الاسم الاول')
    last_name = forms.CharField(label='الاسم الاخير')
    email = forms.CharField(label='البريد الالكتروني',max_length=100,widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ['first_name','last_name','email']

class Profile_update(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']