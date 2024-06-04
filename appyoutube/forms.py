from django import forms
from django.core.exceptions import ValidationError
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['video']

    def clean_video_file(self):
        video = self.cleaned_data.get('video', False)
        if video:
            # Verifica a extensão do arquivo para garantir que seja um vídeo
            if not video.name.endswith(('.mp4', '.avi', '.mov')):
                raise ValidationError("Formato de arquivo não suportado. Apenas arquivos de vídeo (MP4, AVI, MOV) são permitidos.")
            return video
        else:
            raise ValidationError("Nenhum arquivo foi fornecido.")