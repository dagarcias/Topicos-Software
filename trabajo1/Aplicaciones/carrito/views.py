from django.shortcuts import render, redirect
from.models import Carrito
from django.http import HttpResponse
from.forms import *

# Create your views here.
def home(request):
    carritolist=Carrito.objects.all()
    return render(request, "home.html",{"carrito":carritolist})

def listado(request):
    carritolist=Carrito.objects.all()
    return render(request,"listado.html",{"carrito":carritolist})

def creacion(request):
    form=carritoform()

    codigo=request.POST.get('txtCodigo')
    tipodeprenda=request.POST.get('txtPrenda')
    if request.method=='POST':
        form=carritoform(request.POST)
        if form.is_valid():
            print('casivalido')

        else:
            print('valido')
            carrito=Carrito()
            carrito.codigo=codigo
            carrito.tipoDePrenda=tipodeprenda
            carrito.save()
    carritolist=Carrito.objects.all()
    return render(request, "creacion.html",{"carrito":carritolist})


def eliminar(request,codigo):
    carrito = Carrito.objects.get(codigo=codigo)
    carrito.delete()
    redirect('/')
    return render(request,"listado.html")







