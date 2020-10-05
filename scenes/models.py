from django.db import models
from django.urls import reverse
from characters.models import Character

class Scene(models.Model):
    description = models.TextField(default='')
    characters = models.ManyToManyField(Character)

    def __str__(self):
        if(self.id != Null and self.description != Null):
            return self.id + ': ' + self.description
        else:
            return str(self.pk)

    def get_absolute_url(self):
        return reverse('scenes:show-scene', kwargs={'pk': self.pk})
    
    def get_edit_url(self):
        return reverse('scenes:edit-scene', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('scenes:delete-scene', kwargs={'pk': self.pk})

    def get_characters_url(self):
        return reverse('scenes:characters-scene', kwargs={'pk': self.pk})