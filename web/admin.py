from django.contrib import admin
from .models import Genero, Arriendo, Plataforma, Juego

# Register your models here.

admin.site.register(Genero)
admin.site.register(Arriendo)
admin.site.register(Plataforma)
admin.site.register(Juego)
