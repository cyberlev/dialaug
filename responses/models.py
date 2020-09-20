from django.db import models
from django.urls import reverse
from lines.models import Line

class Response(models.Model):
    line = models.ForeignKey(Line, on_delete=models.CASCADE)
    code = models.CharField(max_length=20, default='')
    text = models.TextField(default='')
    
    class Meta:
        ordering = ['code']

    def __str__(self):
        return self.code + ': ' + self.text

    def get_absolute_url(self):
        return reverse("responses:show-thought", kwargs={'pk': self.id})
    
    def get_edit_url(self):
        return reverse("responses:edit-thought", kwargs={'pk': self.id})