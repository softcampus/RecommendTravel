"""ApiServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^test/$', views.test, name='analysis'),
    url(r'^test/test/$', views.test2, name='analysis'),
    url(r'^webhook/$', views.webhook, name='webhook'),
    url(r'^log/$', views.log, name='log'),
    url(r'^select$', views.select, name='select'),
    url(r'^insert$', views.insert, name='insert'),
    url(r'^delete$', views.delete, name='delete'),
    url(r'^drop$', views.drop, name='drop'),
]
