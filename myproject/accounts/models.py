from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    empresa = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20) 
    mensaje = models.TextField(default='') 
   
    def __str__(self):
        return f"{self.nombre}, ({self.empresa})"

class Desarrollador(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    rol = models.CharField(max_length=100)
    proyecto = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre}, ({self.rol})"

class Proyecto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_proyecto = models.CharField(max_length=100)
    descripcion = models.TextField()
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    estado = models.CharField(max_length=50)
    fecha_de_inicio = models.DateField(default=now)
    fecha_de_fin = models.DateField(default=now)
       
    def __str__(self):
        return f"{self.nombre_proyecto}, ({self.cliente}), ({self.estado})"  
        # En accounts/models.py


class FormCliente(models.Model):
    # Definición de campos aquí
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre
      
#class Pag_Proyecto(models.Model):
#    titulo = models.CharField(max_length=200)
 #   descripcion_corta = models.TextField()
#    descripcion_detallada = models.TextField()
#    imagen = models.CharField(max_length=200) 
#    #imagen = models.ImageField(upload_to='portfolio/')
#    cliente = models.CharField(max_length=100, null=True, blank=True)
#    categoria = models.CharField(max_length=100, null=True, blank=True)
#    def __str__(self):
#        return self.titulo

