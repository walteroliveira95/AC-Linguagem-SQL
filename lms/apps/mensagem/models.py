from django.db import models
from aluno.models import Aluno
from professor.models import Professor
import datetime

class Mensagem(models.Model):
     id_aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
     id_professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
     assunto = models.CharField(max_length=100)
     referencia = models.CharField(max_length=150)
     conteudo = models.CharField(max_length=250)
     status = models.CharField(max_length=10, default='Enviado')
     dtEnvio = models.DateField(default=datetime.datetime.today())
     dtResposta = models.DateField()
     resposta = models.CharField(max_length=250)