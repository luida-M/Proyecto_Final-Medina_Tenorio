from django.contrib import admin
from .models import Cliente, Desarrollador

# Register your models here.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'company') 
    ordering = ('id', 'name', 'company')  
    search_fields = ('name', 'company')  
    list_filter = ('company',)    
@admin.register(Desarrollador)
class DesarrolladorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'rol') 
    ordering = ('id', 'name', 'rol')
    search_fields = ('name', 'rol') 
    list_filter = ('rol',)  

