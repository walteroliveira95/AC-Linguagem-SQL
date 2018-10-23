from django.db import models
from accounts.models import User

class Coordenador(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, unique=True)
    celular = models.CharField(max_length=14, unique=True)
   
