from django.db import models
from django.urls import reverse
from characters.models import Character

class Scene(models.Model):
    code = models.CharField(max_length = 12, default='')
    description = models.TextField(blank=True, null=True)
    characters = models.ManyToManyField(Character)

    def get_absolute_url(self):
        return reverse('scenes:show-scene', kwargs={'pk': self.id})