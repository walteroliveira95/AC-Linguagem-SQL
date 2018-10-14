from django.db import models

class Usuario(models.Model):
     login = models.CharField(max_length=100, unique=True)
     senha = models.CharField(max_length=250)
     dtExpiracao = models.DateField(default='1900-01-01')