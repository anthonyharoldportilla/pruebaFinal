from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import  infoUsuarios

# Create your views here.

#listaUsuario = []

def inicio(request):
    return HttpResponse('Bienvenidos a la aplicacion 2')

def ingresoUsuario(request):
    if request.method == 'POST':
        nombreUsuario = request.POST.get('nombreUsuario')
        apellidoUsuario = request.POST.get('apellidoUsuario')
        listaUsuario.append([nombreUsuario,apellidoUsuario])
   
        return HttpResponseRedirect(reverse('app2:ingresoUsuario'))
    return render(request,'ingresoUsuario.html',{
        #'listaUsuarios':listaUsuario,
        'listaUsuarios':infoUsuarios.objects.all().order_by('id'),
    })

def registroCurso(request):
    return render(request,'registroCursos.html')