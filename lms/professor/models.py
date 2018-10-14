from django.db import models
from usuario.models import Usuario

class Professor(models.Model):
     usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
     email = models.EmailField(max_length=30, unique=True)
     celular = models.CharField(max_length=14, unique=True)
     apelido = models.CharField(max_length=10)