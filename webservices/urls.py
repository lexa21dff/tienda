from django.urls import path, include
from rest_framework import routers 
from home.models import *
from webservices.views import *

routers = routers.DefaultRouter()
routers.register(r'productos', producto_viewset)
routers.register(r'marca', marca_viewset)
routers.register(r'categorias', categoria_)

urlpartterns = [
    path('api/', include(routers.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]