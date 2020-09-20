from django.db import models
from django.urls import reverse
from scenes.models import Scene

class Thought(models.Model):
    code = models.CharField(max_length=12, default='')
    scene = models.ForeignKey(Scene, on_delete=models.CASCADE)
    character = models.TextField()
    text = models.TextField()

    class Meta:
        ordering = ['code']

    def __str__(self):
        return self.code + ': ' + self.text

    def get_absolute_url(self):
        return reverse("thoughts:show-thought", kwargs={'pk': self.id})

    def get_edit_url(self):
        return reverse("thoughts:edit-thought", kwargs={'pk': self.id})