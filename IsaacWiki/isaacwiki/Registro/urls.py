from django.urls import path
from .views import (
    RegistroUsuario, 
    TiendaListView, 
    ProductoList, 
    ProductoCreate, 
    ProductoUpdate, 
    ProductoDelete, 
    TiendaCreate, 
    TiendaUpdate, 
    TiendaDelete,
    buscar_tienda,
    detalle_tienda,
    home,
    product_detail,
)

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name="home"),
    path('tiendas/', TiendaListView.as_view(), name="tiendas"),
    path('tiendas/<int:pk>/', detalle_tienda, name="detalle_tienda"),
    path('productos/', ProductoList.as_view(), name="productos"),
    path('product/<int:id>/', product_detail, name='product_detail'),
    path('registrar/', RegistroUsuario.as_view(), name='registrar'),
    path('login/', auth_views.LoginView.as_view(template_name='tienda/login.html'), name='login'),
    path('modificar_producto/<int:pk>', ProductoUpdate.as_view(), name='modificar_producto'),
    path('eliminar_producto/<int:pk>', ProductoDelete.as_view(), name='eliminar_producto'),
    path('agregar_producto/', ProductoCreate.as_view(), name="agregar_producto"),
    path('listar_tienda/', TiendaListView.as_view(), name='listar_tienda'),
    path('modificar_tienda/<int:pk>', TiendaUpdate.as_view(), name='modificar_tienda'),
    path('eliminar_tienda/<int:pk>', TiendaDelete.as_view(), name='eliminar_tienda'),
    path('agregar_tienda/', TiendaCreate.as_view(), name="agregar_tienda"),
    path('buscar_tienda/', buscar_tienda, name="buscar_tienda"),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
