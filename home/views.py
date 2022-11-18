from django.shortcuts import render, redirect
from .models import Producto
from .forms import *
# Create your views here.
def vista_about (request):
    return render (request,'about.html')

def vista_contacto (request):
    info_enviado = False
    email = ""
    title = ""
    text = ""
    if request.method == "POST":
        formulario = contacto_form (request.POST)
        if formulario.is_valid():
            info_enviado = True
            email = formulario.cleaned_data['correo']
            title = formulario.cleaned_data['titulo']
            text = formulario.cleaned_data['texto']
    else:
        formulario = contacto_form()
    return render (request,'contacto.html', locals())


def vista_lista_producto (request):
    lista = Producto.objects.filter()
    print("--------------")
    print(lista)
    print("--------------")
    return render (request,'lista_producto.html', locals())

def vista_agregar_producto (request):
    if request.method == 'POST':
        formulario = agregar_producto_form(request.POST, request.FILES)
        if formulario.is_valid():
            prod = formulario.save(commit = False)
            prod.status = True
            prod.save()
            formulario.save_m2m()
            return redirect ('/lista_producto/')
    else:
        formulario = agregar_producto_form()
    return render (request, 'agregar_producto.html', locals())

def vista_ver_producto (request, id_prod):
    p = Producto.objects.get(id = id_prod)
    return render (request,'ver_producto.html', locals())
