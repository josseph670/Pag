# views.py
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Producto, Tienda
from .forms import RegistroForm, TiendaForm, ProductoForm
from django.contrib.auth.models import User

def home(request):
    return render(request, 'tienda/home.html')

def productos(request):
    return render(request, 'tienda/productos.html')

def tiendas(request):
    return render(request, 'tienda/tiendas.html')

def servicio_web(request):
    return render(request, 'tienda/servicio_web.html')

def formulario(request):
    return render(request, 'tienda/formulario.html')

def login(request):
    return render(request, 'tienda/login.html')

def detalle_tienda(request, pk):
    tienda = get_object_or_404(Tienda, pk=pk)
    productos = tienda.productos.all()
    return render(request, 'tienda/detalle_tienda.html', {'tienda': tienda, 'productos': productos})

def product_detail(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'tienda/product_detail.html', {'producto': producto})

def buscar_tienda(request):
    query = request.GET.get('q')
    if query:
        tienda = get_object_or_404(Tienda, nombre__icontains=query)
        productos = Producto.objects.filter(tienda=tienda)
    else:
        tienda = None
        productos = None
    
    context = {
        'tienda': tienda,
        'productos': productos,
        'tienda_form': TiendaForm(instance=tienda) if tienda else TiendaForm(),
        'producto_form': ProductoForm(),
    }
    return render(request, 'tienda/buscar_tienda.html', context)


class RegistroUsuario(CreateView):
    model = User
    form_class = RegistroForm
    template_name = 'tienda/registrar.html'  # Ajusta 'tu_app' según la estructura de tus archivos
    success_url = reverse_lazy('login')


class ProductoList(ListView):
    model = Producto
    template_name = 'tienda/listar_producto.html'

class ProductoCreate(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'tienda/tiendas.html'
    success_url = reverse_lazy('listar_producto')

class ProductoUpdate(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'tienda/modificar_producto.html'
    success_url = reverse_lazy('listar_producto')

class ProductoDelete(DeleteView):
    model = Producto
    template_name = 'tienda/eliminar_producto.html'
    success_url = reverse_lazy('listar_producto')

class TiendaListView(ListView):
    model = Tienda
    template_name = 'tienda/tiendas.html'
    context_object_name = 'tiendas'

class TiendaCreate(CreateView):
    model = Tienda
    form_class = TiendaForm
    template_name = 'tienda/agregar_tienda.html'
    success_url = reverse_lazy('listar_tienda')

class TiendaUpdate(UpdateView):
    model = Tienda
    form_class = TiendaForm
    template_name = 'tienda/modificar_tienda.html'
    success_url = reverse_lazy('listar_tienda')

class TiendaDelete(DeleteView):
    model = Tienda
    template_name = 'tienda/eliminar_tienda.html'
    success_url = reverse_lazy('listar_tienda')

class TiendaDetailView(DetailView):
    model = Tienda
    template_name = 'tienda/detalle_tienda.html'
    context_object_name = 'tienda'
