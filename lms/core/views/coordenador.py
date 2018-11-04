from django.shortcuts import render
from core.models import Disciplina

def index(request):
     return render(request, 'areas/coordenador/index.html')

def disciplinas(request):
     disciplinas = Disciplina.objects.all()

     return render(request, 'areas/coordenador/disciplinas.html', { 'disciplinas': disciplinas })