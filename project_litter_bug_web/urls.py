"""project_litter_bug_web URL Configuration

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
from django.urls import include

from . import ajax
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', include('content.urls')),
    url('', include('litter.urls')),
    url('', include('script.urls')),
    url(r'^ajax/aggregateData/$', ajax.aggregate_data_handler),
    url(r'^$', views.home, name='home'),
    url(r'^results/$', views.results, name='results'),
    url(r'^about/$', views.about, name='about'),
    url(r'^how-it-works/$', views.how_it_works, name='how-it-works'),
    url(r'^calculation/$', views.calculation, name='calculation'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^donate/$', views.donate, name='donate'),
]
