# accounts/urls.py
from django.urls import path
from . import views  # Si tienes vistas en accounts/views.py

urlpatterns = [
    path('clientes/', views.clientes, name='clientes'),
    path('servicios/', views.servicios, name='servicios'),
    path('vacantes/', views.vacantes, name='vacantes'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('contacto/', views.contacto, name='contacto'),

]
