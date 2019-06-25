from rest_framework import generics

from . import models
from . import serializers


class ScriptList(generics.ListCreateAPIView):
    queryset = models.Script.objects.all()
    serializer_class = serializers.ScriptSerializer


class ScriptDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Script.objects.all()
    serializer_class = serializers.ScriptSerializer
