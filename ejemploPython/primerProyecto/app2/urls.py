from django.urls import path
from . import views

app_name = 'app2'

urlpatterns = [
    path('inicio',views.inicio,name='inicio'),
    path('login',views.ingresoUsuario,name='ingresoUsuario'),
    path('registrocursos',views.registroCursos,name='registroCursos')
]

#http://127.0.0.1:8000/app2/final