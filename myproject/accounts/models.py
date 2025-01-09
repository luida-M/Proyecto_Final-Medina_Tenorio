from django.db import models

class Cliente(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    email = models.EmailField(max_length=100, unique=True, verbose_name="Correo Electrónico")
    company = models.CharField(max_length=100, verbose_name="Empresa", blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")
    is_active = models.BooleanField(default=True, verbose_name="Activo")

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['-date_joined']

    def __str__(self):
        return self.name


class Desarrollador(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    email = models.EmailField(max_length=100, unique=True, verbose_name="Correo Electrónico")
    rol = models.CharField(max_length=100, verbose_name="Rol", blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")
    is_active = models.BooleanField(default=True, verbose_name="Activo")

    class Meta:
        verbose_name = "Desarrollador"
        verbose_name_plural = "Desarrolladores"
        ordering = ['-date_joined']

    def __str__(self):
        return self.name

