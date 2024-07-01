from django import forms
from .models import Trinket
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TrinketForm(forms.ModelForm):
    class Meta:
        model = Trinket
        fields = ['nombre', 'descripcion', 'categoria']


        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripcion',
            'categoria': 'Categoria',


        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')]),
                    }


class RegistroForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
                'username',
                'first_name',
                'last_name',
                'email',
            ]
        labels = {
                'username': 'Nombre de usuario',
                'first_name': 'Nombre',
                'last_name': 'Apellidos',
                'email': 'Correo',
        }