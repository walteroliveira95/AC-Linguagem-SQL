from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

def index_view(request):
     if request.user.is_authenticated:
          return render(request, 'index.html')
     else:
          messages.add_message(request, messages.INFO, 'Você nao esta logado, entre para continuar!')
          return redirect('/accounts/login/')
     