from django.urls import path 
from .views import *
from .models import *
urlpatterns = [
    path('about/',vista_about),
    path('contacto/',vista_contacto),
    #path('usuario', vista_usuario),
    path('lista_producto/',vista_lista_producto, name='lista_producto'),
    path('agregar_producto/',vista_agregar_producto, name='agregar_producto'),
    path('ver_producto/<int:id_prod>/', vista_ver_producto, name='ver_producto'),   
    path('api/', include(routers.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]
