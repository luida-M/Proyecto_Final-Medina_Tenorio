from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    empresa = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20) 
    mensaje = models.TextField(default='') 
   
    def __str__(self):
        return f"{self.name}, ({self.company})"

class Desarrollador(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    rol = models.CharField(max_length=100)
    proyecto = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}, ({self.rol})"

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=50, choices=[
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('completado', 'Completado')
    ])
    cliente = models.CharField(max_length=100)
    image = models.ImageField(upload_to='proyectos/')

    def __str__(self):
        return f"{self.nombre}, ({self.cliente}), ({self.estado})"  
        # En accounts/models.py


class FormCliente(models.Model):
    # Definición de campos aquí
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre
      

