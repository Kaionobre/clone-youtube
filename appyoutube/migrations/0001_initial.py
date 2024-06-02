# Generated by Django 5.0.6 on 2024-06-02 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('video', models.FileField(blank=True, null=True, upload_to='video/')),
            ],
        ),
    ]
