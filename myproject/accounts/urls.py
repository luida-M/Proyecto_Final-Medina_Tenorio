
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

# Desarrollador
urlpatterns += [
    path('desarrollador-list/', views.DesarrolladorListView.as_view(), name="DesarrolladorList"),
    path('desarrollador-detail/<int:pk>/', views.DesarrolladorDetailView.as_view(), name="DesarrolladorDetail"),
    path('desarrollador-create/', views.DesarrolladorCreateView.as_view(), name="DesarrolladorCreate"),
    path('desarrollador-update/<int:pk>/', views.DesarrolladorUpdateView.as_view(), name="DesarrolladorUpdate"),
    path('desarrollador-delete/<int:pk>/', views.DesarrolladorDeleteView.as_view(), name="DesarrolladorDelete"),
]

# Clientes
urlpatterns += [
    path('cliente-list/', views.ClienteListView.as_view(), name="ClienteList"),
    path('cliente-detail/<int:pk>/', views.ClienteDetailView.as_view(), name="ClienteDetail"),
    path('cliente-create/', views.ClienteCreateView.as_view(), name="ClienteCreate"),
    path('cliente-update/<int:pk>/', views.ClienteUpdateView.as_view(), name="ClienteUpdate"),
    path('cliente-delete/<int:pk>/', views.ClienteDeleteView.as_view(), name="ClienteDelete"),
]

# Proyectos
urlpatterns += [
    path('proyectos-list/', views.ProyectoListView.as_view(), name="ProyectoList"),
    path('proyectos-detail/<int:pk>/', views.ProyectoDetailView.as_view(), name="ProyectoDetail"),
    path('proyectos-create/', views.ProyectoCreateView.as_view(), name="ProyectoCreate"),
    path('proyectos-update/<int:pk>/', views.ProyectoUpdateView.as_view(), name="ProyectoUpdate"),
    path('proyectos-delete/<int:pk>/', views.ProyectoDeleteView.as_view(), name="ProyectoDelete"),
]


forms_html = [
    path('form-desarrollador/', views.form_desarrollador, name='form_desarrollador'),
    path('form-cliente/', views.form_cliente, name='form_cliente'),
]

forms_api = [
    path('from-con-api/', views.form_con_api, name='formConApi'),
    path('buscar-form-con-api/', views.buscar_form_con_api, name='Buscar_Form_Con_Api'),
    
]
urlpatterns += forms_html + forms_api
