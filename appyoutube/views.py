from django.shortcuts import render
from.models import Video
from django.views.generic import ListView

class HomeView(ListView):
    model = Video
    template_name = 'modelo/home.html'
    context_object_name = 'Video'

class PerfilView(ListView):
    model = Video
    template_name = 'modelo/perfil.html'
    context_object_name = 'thumb'


