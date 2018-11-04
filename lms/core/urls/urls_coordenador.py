from django.conf.urls import url
from core.views.coordenador import index, disciplinas

app_name = 'coordenador'

urlpatterns = [
     url(r'^$', index, name='index'),
     url(r'^disciplinas$', disciplinas, name='disciplinas'),
]