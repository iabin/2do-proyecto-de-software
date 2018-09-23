from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class SignUpForm(forms.Form):
    nombre = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=30, required=False, help_text='Optional.')
    language = forms.CharField(max_length=254, help_text='Required. Inform a valid email address.')
    birthdate = forms.DateField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('id','name','email','password','language','birthdate')
