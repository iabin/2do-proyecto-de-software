from django import forms
from django.utils.translation import gettext_lazy as _

from aplicacion.models import User



class SignUpForm(forms.ModelForm):
      class Meta:
        model = User

        fields = ('id','name','email','password','language','birthdate','profile_pic')

        labels = {
            'name': _('Nombre'),
            'password': _('Contraseña'),
            'language': _('Idioma'),
            'birthdate': _('Fecha de nacimiento'),
        }

        help_texts = {
            'name': _('Escribe tu nombre'),
        }
        error_messages = {
            'name': {
                'max_length': _("This writer's name is too long."),
            },
        }