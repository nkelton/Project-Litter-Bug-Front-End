from rest_framework import serializers

from . import models


class ScriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Script
        fields = ('id', 'litter_id', 'status', 'download')
