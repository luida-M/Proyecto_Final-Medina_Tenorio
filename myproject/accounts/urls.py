#from accounts.urls.py
from django.urls import path
from accounts import views  # Si tienes vistas en accounts/views.py

urlpatterns = [
    path('', views.base, name='base'),
    path('team/', views.team, name='team'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

]

form_html = [
    path('form-desarrollador/', views.form_desarrollador, name='form_desarrollador'),
    path('form-cliente/', views.form_cliente, name='form_cliente'),
]
urlpatterns += form_html    