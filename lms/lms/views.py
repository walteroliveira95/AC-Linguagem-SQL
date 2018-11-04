from django.shortcuts import render, redirect
from django.contrib.auth.forms import  AuthenticationForm
from core.forms import UserCreationForm
from django.contrib.auth import login
from datetime import date, datetime

def index(request):
    return render(request, 'home/index.html')

def cursos(request):
    return render(request, 'home/cursos.html')

def disciplinas(request):
    return render(request, 'home/disciplinas.html')

def noticias(request):
    return render(request, 'home/noticias.html')


