"""stanhome_mamma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from time import gmtime, strftime
from django.shortcuts import redirect


def handler404(request, ex):
    def get_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    print(strftime("%d/%m/%Y %H:%M:%S", gmtime()),
          get_ip(request),
          request.build_absolute_uri(),
          '404',
          file=open('ip.txt', 'a'))
    return redirect('/')


def handler500(request):
    def get_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    print(strftime("%d/%m/%Y %H:%M:%S", gmtime()),
          get_ip(request),
          request.build_absolute_uri(),
          '500',
          file=open('ip.txt', 'a'))
    return redirect('/')


urlpatterns = [path('admin/', admin.site.urls), path('', include('home.urls'))]
