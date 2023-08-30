from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return HttpResponse('Bienvenidos a la aplicacion 2')

def ingresoUsuario(request):
    listaUsuarios = [
        ['Alexander','Segovia'],
        ['Javier','Hilario'],
        ['Martin','Leyva'],
        ['Juan Diego','Pimentel'],
        ['Diego','Diaz']
    ]
    return render(request,'ingresoUsuario.html',{
        'listaUsuarios':listaUsuarios,
    })