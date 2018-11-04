from django.db import models
from core.models import User

class Aluno(models.Model):
     usuario = models.OneToOneField(User, on_delete=models.PROTECT)
     nome = models.CharField(max_length=30)
     email = models.EmailField(max_length=30, unique=True)
     celular = models.CharField(max_length=14, unique=True)
     ra = models.IntegerField()
     foto = models.CharField(max_length=350, blank=True, default=None)

     def __str__(self):
     	return self.nome