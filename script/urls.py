from rest_framework.urlpatterns import format_suffix_patterns

from django.conf.urls import url

from . import views

urlpatterns = [
    url('script/$', views.ScriptList.as_view()),
    url('script/(?P<pk>\d+)/$', views.ScriptDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
