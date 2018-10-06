from django.db import models

class Usuario(models.Model):
    login = models.CharField(max_length=150)
    senha = models.CharField(max_length=150)
    dt_expiracao = models.DateTimeField()

class Aluno(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    celular = models.CharField(max_length=14)
    ra = models.IntegerField()
    foto = models.CharField(default=None, max_length=500)

class Professor(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    email = models.CharField(max_length=200)
    celular = models.CharField(max_length=14)
    contato = models.CharField(max_length=150)

class Atividade(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.CharField(max_length=250)
    tipo = models.CharField(max_length=15)
    id_professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    descricao = models.CharField(default=None, max_length=150)
    extras = models.CharField(default=None, max_length=50)
