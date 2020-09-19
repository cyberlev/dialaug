from django import forms

from .models import Thought

class ModelThoughtCreateForm(forms.ModelForm):
    character = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Character name"}))
    text = forms.CharField(label='', widget=forms.Textarea(
        attrs={
            "placeholder": "Thought text",
            "rows": 5,
            "cols": 50,
        }
    ))

    class Meta:
        model = Thought
        fields = [
            'character',
            'text',
        ]