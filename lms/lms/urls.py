from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='home'),
    url(r'^cursos/$', views.cursos, name='cursos'),
    url(r'^disciplinas/$', views.disciplinas, name='disciplinas'),
    url(r'^noticias/$', views.noticias, name='noticias'),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^coordenador/', include('apps.coordenador.urls')),
    url(r'^aluno/', include('apps.aluno.urls')),
    url('admin/', admin.site.urls),
]

