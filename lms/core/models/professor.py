from django.db import models
from core.models import User

class Professor(models.Model):
     usuario = models.OneToOneField(User, on_delete=models.CASCADE)
     email = models.EmailField(max_length=30, unique=True)
     celular = models.CharField(max_length=14, unique=True)
     apelido = models.CharField(max_length=10)