from django.conf.urls import url
from . import views

app_name = 'core'

urlpatterns = [
     url(r'^index/$', views.areadoaluno_index, name='index'),
]