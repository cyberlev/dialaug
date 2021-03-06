from django import forms
from responses.models import Response

from .models import Line

class LineCreateForm(forms.Form):
    line_code = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Line code"}))
    line_text = forms.CharField(label='', widget=forms.Textarea(
        attrs={
            "placeholder": "Line text",
            "rows": 5,
            "cols": 50,
        }
    ))

class ModelLineCreateForm(forms.ModelForm):
    class Meta:
        model = Line
        fields = [
            'text',
            'character',
            'scene',
        ]

class AddResponseForm(forms.Form):
    text = forms.CharField()