from django import forms
from django.contrib.auth.forms import UserCreationForm
from aplicacion.models import User



class SignUpForm(forms.ModelForm):
      class Meta:
        model = User

        fields = ('id','name','email','password','language','birthdate')