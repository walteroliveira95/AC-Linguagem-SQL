from django.shortcuts import render
from apps.curso.models import Curso

def homepage(request):
    return render(request, 'home/index.html')

def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'home/cursos.html', { 'cursos': cursos })

def disciplinas(request):
    return render(request, 'home/disciplinas.html')

def noticias(request):
    return render(request, 'home/noticias.html')


