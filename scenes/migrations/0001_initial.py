# Generated by Django 3.1.1 on 2020-09-20 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scene',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character_code', models.CharField(default='', max_length=6)),
                ('scene_number', models.IntegerField(default=0)),
                ('description', models.TextField(blank=True, null=True)),
                ('root_line', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='SceneBuilder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scene_code', models.TextField(default='')),
            ],
        ),
    ]
