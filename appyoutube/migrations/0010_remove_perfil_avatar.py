# Generated by Django 5.0.6 on 2024-06-04 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appyoutube', '0009_remove_perfil_videos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='avatar',
        ),
    ]
