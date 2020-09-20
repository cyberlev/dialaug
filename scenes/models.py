from django.db import models

class Scene(models.Model):
    code = models.CharField(max_length = 12)
    description = models.TextField(blank=True, null=True)