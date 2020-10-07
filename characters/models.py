from django.db import models
from django.urls import reverse

class Character(models.Model):
    name = models.CharField(blank=True, null=True, max_length=80)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    gender = models.CharField(blank=True, null=True, max_length=80)
    code = models.CharField(blank=True, null=True, max_length=6)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name + ' (' + self.code + ')'

    def get_absolute_url(self):
        return reverse("characters:show-character", kwargs={'pk': self.pk})
    
    def get_edit_url(self):
        return reverse("characters:edit-character", kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse("characters:delete-character", kwargs={'pk': self.pk})

    def get_character_code(self):
        if(self.code != None):
            return self.code
        else:
            return 'NONE'