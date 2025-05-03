from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Nombre")
    last_name = models.CharField(max_length=100, verbose_name="Apellido")
    dni = models.CharField(max_length=8, unique=True, null=True, blank=True, verbose_name="DNI")
    phone = models.CharField(max_length=10, verbose_name="Celular")
    province = models.CharField(max_length=100, verbose_name="Provincia")
    locality = models.CharField(max_length=100, null=True, blank=True, verbose_name="Localidad")

    class Meta:
        verbose_name = "cliente"
        verbose_name_plural = "clientes"

    def __str__(self):
        return f"{self.last_name}, {self.first_name} (DNI: {self.dni})"