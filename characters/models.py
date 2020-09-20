from django.db import models

class Character(models.Model):
    first_name = models.CharField(blank=True, null=True, max_length=80, default='UNKNOWN')
    last_name = models.CharField(blank=True, null=True, max_length=80, default='UNKNOWN')
    nickname = models.CharField(blank=True, null=True, max_length=80, default='UNKNOWN')
    birth_date = models.DateField(blank=True, null=True, auto_now=False, auto_now_add=False)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    sex = models.PositiveSmallIntegerField(blank=True, null=True)
    gender = models.CharField(blank=True, null=True, max_length=80, default='UNKNOWN')
    character_code = models.CharField(blank=True, null=True, max_length=6, default='UNKUNK')
    nationality = models.CharField(blank=True, null=True, max_length=2, default='--')
    height = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    skin_color = models.CharField(blank=True, null=True, max_length=80)
    hair_color = models.CharField(blank=True, null=True, max_length=80)
    iris_color = models.CharField(blank=True, null=True, max_length=80)
    description = models.TextField(blank=True, null=True)