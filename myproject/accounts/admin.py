from django.contrib import admin
from .models import Cliente, Desarrollador, Proyecto

# Register your models here.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'email', 'empresa') 
    ordering = ['id', 'empresa'] # Cambiado a lista 
    search_fields = ('nombre', 'empresa') 
    list_filter = ['empresa'] # Cambiado a lista

@admin.register(Desarrollador)
class DesarrolladorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'rol') 
    ordering = ['rol', 'nombre'] # Cambiado a lista 
    search_fields = ('nombre', 'rol') 
    list_filter = ['rol'] # Cambiado a lista

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('nombre_proyecto', 'cliente', 'estado') 
    ordering = ['id', 'nombre_proyecto'] # Cambiado a lista 
    search_fields = ('nombre_proyecto', 'cliente') 
    list_filter = ['estado'] # Cambiado a lista    

#Ir a cada archivo admin.py de cada aplicación y agregamos cada modelo:
# registra los modelos en el panel de administración, pero sin una configuración personalizada de ModelAdmin
#admin.site.register(Pag_Proyecto)
#admin.site.register(Desarrollador)
#admin.site.register(Cliente)
#admin.site.register(Proyecto)
