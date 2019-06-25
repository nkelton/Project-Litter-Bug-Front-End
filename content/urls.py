from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url('content/$', views.ContentList.as_view()),
    url('content/(?P<litter_id>\d+)/$', views.ContentRetrieveAndDelete.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
