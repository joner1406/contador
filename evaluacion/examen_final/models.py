from django.db import models
# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    rol = models.CharField(max_length=50)
    correo = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre