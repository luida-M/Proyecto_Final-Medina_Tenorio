from django.db import models
class Cliente(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    company = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20) 
    mensaje = models.TextField(default='') 
    def __str__(self):
        return self.name
class Desarrollador(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    rol = models.CharField(max_length=100)
    proyecto = models.CharField(max_length=100)

    def __str__(self):
        return self.name

