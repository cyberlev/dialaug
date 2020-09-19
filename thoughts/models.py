from django.db import models
from django.urls import reverse

class Thought(models.Model):
    character = models.TextField()
    text = models.TextField()

    def get_absolute_url(self):
        return reverse("thoughts:show-thought", kwargs={'pk': self.id})