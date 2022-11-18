from rest_framework import serializer
from home.models import *

class producto_serializer(serializer.HyperLiinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ('url', 'nombre', 'descripcion', 'status', 'foto', 'precio', 'stock', 'marca', 'categorias')
class producto_serializer(serializer.HyperLiinkedModelSerializer):
    class Meta:
        model = Marca
        fields = ('url', 'id', 'nombre',)
class producto_serializer(serializer.HyperLiinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ('url', 'nombre',)
