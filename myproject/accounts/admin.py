from django.contrib import admin
from .models import Cliente, Desarrollador, Proyecto

# Register your models here.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'empresa') 
    ordering = ('id', 'nombre', 'empresa')  
    search_fields = ('nombre', 'empresa')  
    list_filter = ('empresa',)    

@admin.register(Desarrollador)
class DesarrolladorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'rol') 
    ordering = ('id', 'nombre', 'rol')
    search_fields = ('nombre', 'rol') 
    list_filter = ('rol',)  

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'cliente', 'estado') 
    ordering = ('id', 'nombre')
    search_fields = ('nombre', 'cliente') 
    list_filter = ('estado',)      

#Ir a cada archivo admin.py de cada aplicación y agregamos cada modelo:
#admin.site.register(Desarrollador)
#admin.site.register(Cliente)
#admin.site.register(Proyecto)
