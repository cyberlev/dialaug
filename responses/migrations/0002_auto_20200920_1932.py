# Generated by Django 3.1.1 on 2020-09-20 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('responses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='code',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='response',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
