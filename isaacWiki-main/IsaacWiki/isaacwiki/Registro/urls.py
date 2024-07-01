from django.urls import path, include
from . import views
from .views import RegistroUsuario

urlpatterns = [
    path('', views.home, name= "home"),
    path('bosses', views.bosses, name="bosses"), 
    path('items', views.items, name="items"), 
    path('personajes', views.personajes, name="personajes"), 
    path('servicio_web', views.servicio_web, name="servicio_web"), 
    path('formulario', views.formulario, name="formulario"), 
    # Clases Generics
    path('registrar', RegistroUsuario.as_view(), name="registrar"),
    path('listar_trinket/', views.TrinketList.as_view(), name='listar_trinket'),
    path('modificar_trinket/<int:pk>', views.TrinketUpdate.as_view(), name='modificar_trinket'),
    path('eliminar_trinket/<int:pk>', views.TrinketDelete.as_view(), name='eliminar_trinket'),
    path('agregar_trinket', views.TrinketCreate.as_view(), name="agregar_trinket"),

    
    
]


