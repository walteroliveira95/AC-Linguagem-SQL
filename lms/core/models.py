from django.db import models

class Aluno(models.Model):
    id_usuario = models.ForeignKey('', on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    celular = models.CharField(max_length=14)
    ra = models.IntegerField()
    foto = models.CharField(default=None, max_length=500)
