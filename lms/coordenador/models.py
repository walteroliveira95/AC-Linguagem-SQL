from django.db import models
from usuario.models import Usuario

class Coordenador(models.Model):
     id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
     nome = models.CharField(max_length=30)
     email = models.EmailField(max_length=30, unique=True)
     celular = models.CharField(max_length=14, unique=True)
     
