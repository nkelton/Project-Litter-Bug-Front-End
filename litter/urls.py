from rest_framework.urlpatterns import format_suffix_patterns

from django.conf.urls import url

from . import views

urlpatterns = [
    url('litter/$', views.LitterList.as_view()),
    url('litter/(?P<litter_id>\d+)/$', views.LitterDetailByLitterId.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
