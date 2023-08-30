from django.urls import path
from . import views

app_name = 'app1'

urlpatterns = [
    path('',views.index,name='index'),
    path('pucp-django',views.ejemplo,name='ejemplo'),
    path('cetam-django',views.cetam,name='cetam')
]