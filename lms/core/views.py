from django.shortcuts import render, redirect
from django.contrib import messages

def areadoaluno_index(request):
	if request.user.is_authenticated:
		user = request.user
	else:
		messages.add_message(request, messages.INFO, 'Você nao esta logado, entre com sua conta para continuar.')
		return redirect('/accounts/login')

	return render(request, 'index.html', { 'user': user })