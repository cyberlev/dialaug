from django import forms

from .models import Scene

class SceneCreateForm(forms.ModelForm):
    class Meta:
        model = Scene
        fields = [
            'description',
            'characters',
        ]

class AddLineForm(forms.Form):
    character = forms.IntegerField()
    text = forms.CharField()