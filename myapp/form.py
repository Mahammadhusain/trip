from django import forms
from django.contrib.auth.forms import (UserCreationForm,AuthenticationForm,
UserChangeForm, PasswordChangeForm,PasswordResetForm,SetPasswordForm)
from django.contrib.auth.models import User
from .models import BookingModel

class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Confirm-Password'}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2',]
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter User Name'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter E-Mail'}),
        }


class UserProfileChangeForm(UserChangeForm):
    password =None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}),
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last Name'}),
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter E-Mail'}),
        }


class PassChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Old Password'}))
    new_password1 =forms.CharField(label='New Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter New Password'}))
    new_password2 =forms.CharField(label='Confirm New Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Re-New Password'}))

# Email TextBox Send With Registred E-Mail
class PassResetForm(PasswordResetForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Your Registered E-Mail'}))

# New Password Set Registred E-Mail Link
class SetNewPassForm(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter New Password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm New Password'}))



class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','password']


gender = (('Male','Male'),('Female','Female'))

class BookingForm(forms.ModelForm):
    class Meta:
        model=BookingModel
        fields = ['fname','lname','mobile',
                    'email','gender',]
        
        widgets={
            # 'user':forms.TextInput(attrs={'class':'form-control'}),
            'fname':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Firstname','required':True}),
            'lname':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Lastname'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Mobile Number'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email'}),
            'gender':forms.Select(choices=gender,attrs={'class':'form-control'}),
            
        }


