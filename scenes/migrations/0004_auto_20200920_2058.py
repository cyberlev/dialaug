# Generated by Django 3.1.1 on 2020-09-20 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenes', '0003_scene_characters'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scene',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
