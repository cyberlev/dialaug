from django.db import models
from django.urls import reverse
from lines.models import Line
from scenes.models import Scene

class Response(models.Model):
    line = models.ForeignKey(Line, on_delete=models.PROTECT)
    next_line = models.OneToOneField(Line, related_name="next_line", on_delete=models.PROTECT, null=True)
    text = models.TextField(default='')
    
    class Meta:
        ordering = ['pk']

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse("responses:show-response", kwargs={'pk': self.pk})
    
    def get_edit_url(self):
        return reverse("responses:edit-response", kwargs={'pk': self.pk})

    def get_response_code(self):
        return self.line.get_line_code() + '-' + 'R' + self.pk