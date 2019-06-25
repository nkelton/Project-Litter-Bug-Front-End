from rest_framework import serializers

from . import models


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Content
        fields = ('id', 'litter_id', 'url', 'type')