from rest_framework import serializers

from . import models


class LitterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Litter
        fields = ('id', 'litter_id', 'title', 'url', 'weight')