from django.db import models
from django.urls import reverse
from scenes.models import Scene
from characters.models import Character

class Line(models.Model):
    scene = models.ForeignKey(Scene, on_delete=models.CASCADE, default=None, null=True)
    character = models.ForeignKey(Character, on_delete=models.CASCADE, null=True)
    code = models.CharField(max_length=80, null=True)
    text = models.TextField(default='')

    class Meta:
        ordering = ['code']

    def __str__(self):
        return self.code + ': ' + self.text

    def get_absolute_url(self):
        return reverse("lines:show-line", kwargs={'pk': self.id})

    def get_edit_url(self):
        return reverse("lines:edit-line", kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse("lines:delete-line", kwargs={'pk': self.id})