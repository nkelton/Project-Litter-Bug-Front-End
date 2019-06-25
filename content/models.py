from django.db import models


class Content(models.Model):
    litter_id = models.BigIntegerField()
    url = models.TextField()
    type = models.TextField()
