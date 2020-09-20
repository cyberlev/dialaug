# Generated by Django 3.1.1 on 2020-09-20 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0002_auto_20200920_1606'),
        ('lines', '0003_auto_20200920_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='line',
            name='character',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='characters.character'),
        ),
    ]
