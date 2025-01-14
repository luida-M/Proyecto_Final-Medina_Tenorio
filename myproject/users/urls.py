from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views 
from .views import CambiarPasswdView

urlpatterns = [
    path('login/', views.login_request, name="Login"),
    path('register/', views.register, name="Register"),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name="Logout"),
    path('edit/', views.edit, name="Editar"),
    path('cambiar_passwd/', views.CambiarPasswdView.as_view(), name="CambiarPasswd"),
]