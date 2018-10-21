from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='home'),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^area/', include('core.urls')),
    url('admin/', admin.site.urls),
]

