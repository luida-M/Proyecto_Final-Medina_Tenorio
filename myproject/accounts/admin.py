from django.contrib import admin
from .models import Cliente, Desarrollador

# Register your models here.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "company"] 
    ordering = ["name", "company",]   
@admin.register(Desarrollador)
class DesarrolladorAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "rol"] 
    ordering = ["name", "rol",]




