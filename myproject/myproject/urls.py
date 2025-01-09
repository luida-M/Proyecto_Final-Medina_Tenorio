"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('myproject/', include('myproject.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from accounts import views as accounts_views
#from accounts import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta para el panel de administración
    path('accounts/', include('accounts.urls')),  # Incluye las rutas de 'accounts'
    #path('base/', views.base),  # Ruta directa para la vista 'base_view'
]

# Servir archivos estáticos durante el desarrollo
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
