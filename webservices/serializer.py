from home.models import * 
from .serializer import *
from rest_framework import viewsets

class producto_viewset (viewsets.ModelViewset):
    queryset = Producto.objects.all()
    serializer_class = producto_serializer

class marca_viewset (viewsets.ModelViewset):
    queryset = Marca.objects.all()
    serializer_class = marca_serializer

class producto_viewset (viewsets.ModelViewset):
    queryset = Categoria.objects.all()
    serializer_class = categoria_serializer

