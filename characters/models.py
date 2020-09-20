from django.db import models

class Character(models.Model):
    name = models.CharField(blank=True, null=True, max_length=80)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    code = models.CharField(blank=True, null=True, max_length=6)
    description = models.TextField(blank=True, null=True)