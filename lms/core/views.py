from django.shortcuts import render, redirect
from django.contrib import messages

def areadoaluno_index(request):
	user = None

	print(request.user.is_authenticated)

	if request.user.is_authenticated:
		user = request.user
	else:
		print('fdsf')
		messages.add_message(request, messages.INFO, 'Você nao esta logado, entre com sua conta para continuar.')
		return redirect('/accounts/login')

	return render(request, 'index.html', { 'user': user })