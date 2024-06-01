from django.db import models


class Video(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    video = models.FileField(upload_to='video/',null=True, blank=True)
 
    def __str__(self):
        return self.title
