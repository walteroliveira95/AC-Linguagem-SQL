from django.contrib import messages
from apps.coordenador.models import Coordenador
from apps.aluno.models import Aluno
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, update_session_auth_hash
from datetime import date, datetime

def signup_view(request):
     if request.method == 'POST':
          form = UserCreationForm(request.POST)
          if form.is_valid():
               user = form.save()
               login(request, user)
               return redirect('/')
     else:
          form = UserCreationForm()

     return render(request, 'accounts/signup.html', { 'form': form })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            if user.dtExpiracao == date(1900, 1, 1):
                return redirect('/accounts/changepassword/')

            print()

            veiry_account_type(user)
            

            if Coordenador.objects.filter(usuario = user).count() > 0:
                return redirect('/coordenador')
            if Aluno.objects.filter(usuario = user).count() > 0:
                return redirect('/aluno/')

            
    else:
        form = AuthenticationForm()
          
    return render(request, 'registration/login.html', { 'form': form })

def logout_user(request):
    logout(request)
    return redirect('/accounts/login')

def index(request):
    return login_view(request)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            user.dtExpiracao = '2018-01-01'
            user.save()

            messages.success(request, 'fdsfdf')
            return redirect('/accounts/login')
        else:
            messages.error(request, 'fdsfdsfdgd')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'registration/changepassword.html', { 'form': form })


def veiry_account_type(user):
    pass