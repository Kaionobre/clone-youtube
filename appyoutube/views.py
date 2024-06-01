from django.shortcuts import render
from.models import Video
from django.views.generic import DetailView, ListView

class BaseView(ListView):
    model = Video
    template_name = 'base.html'

class PerfilView(ListView):
    model = Video
    template_name = 'modelo/perfil.html'


