# Generated by Django 3.1.1 on 2020-09-20 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0002_auto_20200920_1606'),
        ('scenes', '0002_auto_20200920_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='scene',
            name='characters',
            field=models.ManyToManyField(to='characters.Character'),
        ),
    ]
