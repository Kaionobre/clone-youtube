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
    paginate_by = 3

class ConsultaView(ListView):
    model = Video
    template_name = 'modelo/pesquisa.html'
    context_object_name = 'objects'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(titulo__icontains=query)
        return queryset
