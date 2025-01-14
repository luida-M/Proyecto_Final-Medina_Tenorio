from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Imagen(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    imagen = models.ImageField(upload_to='imagenes', null=True, blank = True)

    def __str__(self):
        return f"{settings.MEDIA_URL}{self.imagen}"

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    imagen = models.ImageField(upload_to="avatares", blank=True, null=True)
   
    def __str__(self):
        return f"{self.user} - {self.imagen}"