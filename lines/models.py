from django.db import models
from django.urls import reverse
from scenes.models import Scene
from characters.models import Character
from django.contrib.auth.models import User

class Line(models.Model):
    scene = models.ForeignKey(Scene, on_delete=models.CASCADE, default=None, null=True)
    character = models.ForeignKey(Character, on_delete=models.CASCADE, null=True)
    text = models.TextField(default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        ordering = ['pk']

    def __str__(self):
        if(self.pk != None and self.text != None):
            return str(self.pk) + ': ' + self.text
        else:
            return "NO ID"

    def get_absolute_url(self):
        return reverse("lines:show-line", kwargs={'pk': self.pk})

    def get_edit_url(self):
        return reverse("lines:edit-line", kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse("lines:delete-line", kwargs={'pk': self.pk})

    def get_line_code(self):
        return 'S' + str(self.scene.pk) + '-' + self.character.code + '-L' + str(self.pk)

    def get_line_id(self):
        return 'L' + str(self.pk)