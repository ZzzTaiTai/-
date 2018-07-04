"""Emoji URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
#import view
from django.conf.urls.static import static
from django.conf import settings
from . import views as v
app_name='E_emoji'
urlpatterns = [
    url(r'^$',v.index,name='index'),#首页
    url(r'^upload',v.uploadimg,name='upload'),
    url(r'^show', v.showimg,name='show'),
    #url(r'^makeit$',v.makeit),#生成表情包的接口
    #url(r'^about$',v.about), #关于页面
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
