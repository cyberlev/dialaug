# Generated by Django 3.1.1 on 2020-09-20 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scenes', '0003_scene_characters'),
        ('lines', '0002_auto_20200920_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='line',
            name='scene',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='scenes.scene'),
        ),
    ]
