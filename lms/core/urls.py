from django.conf.urls import url
from . import views

app_name = 'core'

urlpatterns = [
     url(r'^$', views.areadoaluno_index, name='index'),
     url(r'^aluno/$', views.areadoaluno_index, name='aluno'),
     url(r'^coordenador/$', views.areadoaluno_index, name='coordenador'),
]