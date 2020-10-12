from django import forms

from .models import Response

class ResponseCreateForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = [
            'text',
        ]

class AddConsequenceForm(forms.Form):
    character = forms.IntegerField()
    text = forms.CharField()