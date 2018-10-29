from django.db import models
from apps.coordenador.models import Coordenador
from apps.professor.models import Professor
from apps.curso.models import Curso
from apps.aluno.models import Aluno
from django.utils import timezone

class Disciplina(models.Model):
     nome = models.CharField(max_length=30, unique=True)
     data = models.DateField(default=timezone.now)
     status = models.CharField(max_length=7, default='ABERTA')
     planoDeEnsino = models.TextField()
     cargaHoraria = models.IntegerField()
     competencias = models.CharField(max_length=30)
     habilidade = models.CharField(max_length=30)
     ementa = models.CharField(max_length=30)
     conteudoProgramatico = models.CharField(max_length=30)
     bibliografiaBasica = models.CharField(max_length=30)
     bibliografiaComplementar = models.CharField(max_length=30)
     percentualPatrico = models.IntegerField()
     percentualTeorico = models.IntegerField()
     coordenador = models.ForeignKey(Coordenador, on_delete=models.CASCADE)

class DisciplinaOferatada(models.Model):
     coordenador = models.ForeignKey(Coordenador, on_delete=models.CASCADE)
     dtInicioMatricula = models.DateField(default=None)
     dtFimMatricula = models.DateField(default=None)
     disciplina = models.ForeignKey(Disciplina, on_delete=classmethod)
     curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
     ano = models.IntegerField()
     semetre = models.IntegerField()
     Turma = models.CharField(max_length=1)
     professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
     metodologia = models.CharField(max_length=250, default=None)
     recursos = models.CharField(max_length=100, default=None)
     criterioAvaliacao = models.CharField(max_length=100, default=None)
     planoDeAulas = models.CharField(max_length=100, default=None)

class SolicitacaoMatricula(models.Model):
     aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
     disciplina = models.ForeignKey(Disciplina, on_delete=classmethod)
     dtSolicitacao = models.DateField(default=timezone.now)
     coordernador = models.ForeignKey(Coordenador, default=None, on_delete=models.CASCADE)
     status = models.CharField(max_length=10, default='Solicitada')

