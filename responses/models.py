from django.db import models
from lines.models import Line

class Response(models.Model):
    line = models.ForeignKey(Line, on_delete=models.CASCADE)
    # next_line = models.ForeignKey(Line, on_delete=models.CASCADE)
    code = models.CharField(max_length=20, default='')
    text = models.TextField(default='')
    
    class Meta:
        ordering = ['code']

    def __str__(self):
        return self.code + ': ' + self.text