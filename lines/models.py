from django.db import models
from django.urls import reverse

class Line(models.Model):
    code = models.CharField(max_length=80, null=True)
    text = models.TextField()

    def get_absolute_url(self):
        return reverse("lines:show-line", kwargs={'pk': self.id})

    def get_edit_url(self):
        return reverse("lines:edit-line", kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse("lines:delete-line", kwargs={'pk': self.id})