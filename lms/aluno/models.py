from django.db import models
from usuario.models import Usuario

class Aluno(models.Model):
     id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
     nome = models.CharField(max_length=30)
     email = models.EmailField(max_length=30, unique=True)
     celular = models.CharField(max_length=14, unique=True)
     ra = models.IntegerField()
     foto = models.CharField(max_length=350, default=None)
