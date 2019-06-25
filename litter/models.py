from django.db import models


class Litter(models.Model):
    litter_id = models.BigIntegerField()
    title = models.TextField()
    url = models.TextField()
    weight = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)