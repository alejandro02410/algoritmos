from django.urls import path
from . import views

urlpatterns = [

    path('prueba2/', views.muestra_datos, name='prueba2'),

]