from django.contrib import admin
from django.conf.urls import url, include
from .  import views
from core.views import login_view, signup_view, change_password, logout_user

app_name = 'lms'

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^cursos$', views.cursos, name='cursos'),
    url(r'^disciplinas$', views.disciplinas, name='disciplinas'),
    url(r'^noticias$', views.noticias, name='noticias'),
    url(r'^login$', login_view, name='login'),
    url(r'^logout$', logout_user, name='logout'),
    url(r'^criarconta$', signup_view, name='signup'),
    url(r'^login/changepassword/$', change_password, name='changepassword'),
    url(r'^coordenador/', include('core.urls.urls_coordenador')), 
    url('admin/', admin.site.urls),
]
