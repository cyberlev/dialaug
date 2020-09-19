from django.db import models

class Scene(models.Model):
    character_code = models.CharField(max_length = 6, default='')
    scene_number = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    root_line = models.TextField(default='')

class SceneBuilder(models.Model):
    scene_code = models.TextField(default='')