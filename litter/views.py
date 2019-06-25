from rest_framework import generics

from . import models
from . import serializers


class LitterList(generics.ListCreateAPIView):
    queryset = models.Litter.objects.all()
    serializer_class = serializers.LitterSerializer


class LitterDetailByLitterId(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Litter.objects.all()
    serializer_class = serializers.LitterSerializer
    # lookup_field = 'litter_id'

    def get_object(self):
        litter_id = self.kwargs['litter_id']
        return models.Litter.objects.get(litter_id=litter_id)
