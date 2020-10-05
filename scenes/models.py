from django.db import models
from django.urls import reverse
from characters.models import Character

class Scene(models.Model):
    description = models.TextField(default='')
    characters = models.ManyToManyField(Character)

    def __str__(self):
        if(self.pk != None and self.description != None):
            return 'S' + str(self.pk) + ': ' + self.description
        else:
            return "NO ID"

    def get_absolute_url(self):
        return reverse('scenes:show-scene', kwargs={'pk': self.pk})
    
    def get_edit_url(self):
        return reverse('scenes:edit-scene', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('scenes:delete-scene', kwargs={'pk': self.pk})

    def get_characters_url(self):
        return reverse('scenes:characters-scene', kwargs={'pk': self.pk})

    def get_scene_code(self):
        return 'S' + str(self.pk)