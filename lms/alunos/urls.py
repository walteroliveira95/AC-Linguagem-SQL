from django.conf.urls import url
from . import views

app_name = 'alunos'

urlpatterns = [
    url(r'^index/$', views.index_view, name='index'),
]