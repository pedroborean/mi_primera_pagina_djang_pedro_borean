# Generated by Django 5.1.4 on 2024-12-09 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_blogs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='creacion',
            new_name='fecha_publicacion',
        ),
    ]