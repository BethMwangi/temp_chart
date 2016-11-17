"""django_app URL Configuration

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
from django.conf.urls import url, include

from django.contrib import admin
from temp_app.views import *
from temp_app.views import list_temp
import temp_app
from temp_app import views, models
from django.views.generic import TemplateView



urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', temp_app.views.main_page ,name='main_page'),
    url(r'^list_temp/$', temp_app.views.list_temp , name='list_temp'),

    ]
