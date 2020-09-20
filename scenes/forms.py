from django import forms

from .models import Scene

class SceneCreateForm(forms.ModelForm):
    class Meta:
        model = Scene
        fields = [
            'code',
            'description',
        ]