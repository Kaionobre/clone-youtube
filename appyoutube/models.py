from django.db import models
from django.contrib.auth.models import User

class Video(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    video = models.FileField(upload_to='video/',null=True, blank=True)
    thumbnail = models.ImageField(upload_to='thumbnails/',null=True, blank=True)

    def __str__(self):
        return self.titulo
