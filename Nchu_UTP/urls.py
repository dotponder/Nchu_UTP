"""Nchu_UTP URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import RedirectView
from django.views.static import serve
from Nchu_UTP import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('goods', include('goods.urls')),
    path('user', include('user.urls')),
    path('order', include('order.urls')),
    path('favicon.ico',RedirectView.as_view(url='static/image/favicon.ico')),
    path('tinymce/', include('tinymce.urls')),
    url(r'^media/(?P<path>.*)',serve,{'document_root':settings.MEDIA_ROOT})
    #path('media/<path>',serve,{'document_root':settings.MEDIA_ROOT})
]
