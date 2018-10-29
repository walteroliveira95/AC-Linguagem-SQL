from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),
    url(r'^signup/$', views.signup_view, name="signup"),
    url(r'^changepassword/$', views.change_password, name="change_pass")
]
