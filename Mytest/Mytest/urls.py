"""Mytest URL Configuration

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
from web01.views import main,common

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', common.Login.as_view()),
    url(r'^logout/', common.logout),
    url(r'^adduser/$', main.adduser),
    url(r'^host_group/$', main.Host_group.as_view()),
    url(r'^idc/$', main.Idc.as_view()),
    url(r'^host/$', main.Host.as_view()),
    url(r'^user/$', main.User.as_view()),
    url(r'^log/$', main.Log.as_view()),
    url(r'^add_host/$', main.Add_host.as_view()),
    url(r'^host/details/(?P<id>\d+)', main.HostDetails.as_view()),
    # url(r'^test/', main.test),
]
