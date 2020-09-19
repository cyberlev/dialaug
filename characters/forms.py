from django import forms

from .models import Character

class CharacterCreateForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = [
            'first_name',
            'last_name',
            'nickname',
            'birth_date',
            'age',
            'sex',
            'gender',
            'character_code',
            'nationality',
            'height',
            'weight',
            'skin_color',
            'hair_color',
            'iris_color',
            'description',
        ]

class RawCharacterCreateForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    nickname = forms.CharField()
    birth_date = forms.DateField()
    age = forms.IntegerField()
    sex = forms.IntegerField()
    gender = forms.CharField()
    character_code = forms.CharField()
    nationality = forms.CharField()
    height = forms.FloatField()
    weight = forms.FloatField()
    skin_color = forms.CharField()
    iris_color = forms.CharField()
    description = forms.CharField()