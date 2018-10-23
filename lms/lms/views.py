from django.shortcuts import render

def homepage(request):
     return render(request, 'home/index.html')

def cursos(request):
     return render(request, 'home/cursos.html')

def disciplinas(request):
     return render(request, 'home/disciplinas.html')

def noticias(request):
     return render(request, 'home/noticias.html')
