# Generated by Django 5.0.6 on 2024-06-04 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appyoutube', '0006_remove_video_perfil_perfil_videos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='videos',
        ),
    ]