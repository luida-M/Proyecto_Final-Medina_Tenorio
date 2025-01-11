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

forms_api = [
    path('from-con-api/', views.form_con_api, name='formConApi'),
    path('buscar-form-con-api/', views.buscar_form_con_api, name='Buscar_Form_Con_Api'),
    
]
urlpatterns += form_html + forms_api
