from django.db import models
from professor.models import Professor
from disciplina.models import DisciplinaOferatada
from aluno.models import Aluno
from django.utils import timezone

class Atividade(models.Model):
     titulo = models.CharField(max_length=20, unique=True)
     descricao = models.CharField(max_length=255, default=None)
     conteudo = models.CharField(max_length=255)
     tipo = models.CharField(max_length=15)
     extrar = models.CharField(max_length=255, default=None)
     id_professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

class AtividadeVinculada(models.Model):
     id_atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE)
     id_professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
     id_disciplinaOfertada = models.ForeignKey(DisciplinaOferatada, on_delete=models.CASCADE)
     rotulo = models.CharField(max_length=4)
     status = models.CharField(max_length=15)
     dtInicioRespostas = models.DateField()
     dtFimRespostas = models.DateField()


class Entrega(models.Model):
     id_aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
     id_atividadeVinculada = models.ForeignKey(AtividadeVinculada,on_delete=models.CASCADE)
     titulo = models.CharField(max_length=50)
     resposta = models.CharField(max_length=250)
     dtEntrega = models.DateField(default=timezone.now)
     status = models.CharField(max_length=9, default='Entregue')
     id_professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
     nota = models.FloatField(default=None)
     dtAvaliacao = models.DateField(default=None)
     obs = models.CharField(max_length=150, default=None)
