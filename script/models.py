from django.db import models


class Script(models.Model):
    litter_id = models.BigIntegerField()
    status = models.TextField()
    download = models.IntegerField()
