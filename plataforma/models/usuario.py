# plataforma/models/usuario.py

from django.db import models

class Usuario(models.Model):
    usuario = models.CharField(max_length=150)
    email = models.EmailField()
    # otros campos que necesites

    def __str__(self):
        return self.usuario
