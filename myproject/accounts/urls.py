#from accounts.urls.py
from django.urls import path
from . import views  # Si tienes vistas en accounts/views.py

urlpatterns = [
    path('', views.base, name='base'),
    path('team/', views.team, name='team'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('desarrollador/', views.desarrollador, name='desarrollador'),
    path('cliente/', views.cliente, name='cliente'),

]

form_html = [
    path('desarrollador/', views.desarrollador, name='desarrollador'),
    path('form_cliente/', views.cliente, name='from_cliente'),
]
urlpatterns += form_html    