from django.contrib.auth.forms import UserCreationForm
from . models import *
from django import forms

class CustomUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Enter User Name'
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class':'form-control',
            'placeholder':'Enter Email Address'
        }
    ))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'Enter Your Password'
        }
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'Enter Your Confirm Password'
        }
    ))
    class Meta:
        model = User
        fields =['username','email','password1','password2']

class ShippingAddressForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Full Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last Name'}))
    address_line1 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'address_line1'}))
    address_line2 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'address_line2'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'city'}))
    state = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'state'}))
    postal_code = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'postal_code'}))
    country = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'country'}))
    phone_number = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter phone_number'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter email'}))
    class Meta:
        model = ShippingAddress
        fields = ['first_name', 'last_name', 'address_line1', 'address_line2', 'city', 'state', 'postal_code', 'country', 'phone_number', 'email']
