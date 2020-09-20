from django import forms

from .models import Character

class CharacterCreateForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = [
            'name',
            'age',
            'gender',
            'code',
            'description',
        ]

class RawCharacterCreateForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    gender = forms.CharField()
    code = forms.CharField()
    description = forms.CharField()