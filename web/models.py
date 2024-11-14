from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Genero(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Plataforma(models.Model):
    nombre = models.CharField(max_length=50)
    dias_arriendo = models.IntegerField()
    precio_dias_atraso = models.IntegerField()

    def __str__(self):
        return self.nombre

class Juego(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    anno = models.IntegerField()
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    plataforma = models.ForeignKey(Plataforma, on_delete=models.CASCADE)
    arrendador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.titulo} - {self.anno} - {self.genero} - {self.plataforma}"

class Arriendo(models.Model):
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_arriendo = models.DateTimeField(default=timezone.now)
    fecha_devolucion = models.DateTimeField(null=True, blank=True)
    multa = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} - {self.juego.titulo}'