from django.db import models
from django.urls import reverse
from lines.models import Line
from scenes.models import Scene

class Response(models.Model):
    scene = models.ForeignKey(Scene, on_delete=models.CASCADE, null=True)
    line = models.ForeignKey(Line, on_delete=models.CASCADE)
    next_line = models.OneToOneField(Line, related_name="next_line", on_delete=models.CASCADE, null=True)
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