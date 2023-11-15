from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser

#Clase para usuarios
class User(AbstractUser):
    def __str__(self):
        return self.username

#Clase para notas registradas del usuario
class Nota(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nota = models.IntegerField(default=0)
    fecha_evaluacion = models.DateTimeField()

    def __str__(self):
        return f"{self.usuario.username} - {self.nota} - {self.fecha_evaluacion}"
