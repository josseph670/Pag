from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Tienda, Producto

class TiendaForm(forms.ModelForm):
    class Meta:
        model = Tienda
        fields = ['nombre', 'descripcion', 'estado', 'tiempo_espera_min', 'tiempo_espera_max', 'imagen']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'tienda', 'imagen']



class RegistroForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        labels = {
                'username': 'Nombre de usuario',
                'first_name': 'Nombre',
                'last_name': 'Apellidos',
                'email': 'Correo',
        }
        