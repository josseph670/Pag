from django.shortcuts import render
from .models import Trinket
from .forms import TrinketForm
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import RegistroForm


def home(request):
    return render(request, 'Registro/home.html')

def bosses(request):
    return render(request, 'Registro/bosses.html')

def items(request):
    return render(request, 'Registro/items.html')

def personajes(request):
    return render(request, 'Registro/personajes.html')

def servicio_web(request):
    return render(request, 'Registro/servicio_web.html')

def formulario(request):
    return render(request, 'Registro/formulario.html')

class RegistroUsuario(CreateView):
    model = User
    template_name = "Registro/registrar.html"
    form_class = RegistroForm
    success_url = reverse_lazy('home')
    

class TrinketUpdate(UpdateView):
    model = Trinket
    form_class = TrinketForm
    template_name = 'Registro/modificar_trinket.html'
    success_url = reverse_lazy('listar_trinket')

class TrinketDelete(DeleteView):
    model = Trinket
    template_name = 'Registro/eliminar_trinket.html'
    success_url = reverse_lazy('listar_trinket')

class TrinketList(ListView):
    model = Trinket
    template_name = 'Registro/listar_trinket.html'

class TrinketCreate(CreateView):
    model = Trinket
    form_class = TrinketForm
    template_name = 'Registro/agregar_trinket.html'
    success_url = reverse_lazy("listar_trinket")
