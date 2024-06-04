from django.shortcuts import render
from accounts.forms import CadastroForms
from.models import Video, Perfil
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy



class HomeView(ListView):
    model = Video
    template_name = 'modelo/home.html'
    context_object_name = 'Video'
    login_url = '/cadastro/'

class PerfilView(LoginRequiredMixin, ListView):
    model = Perfil
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
    
class OrdenacaoView(ListView):
    model = Video
    template_name = 'modelo/ordenacao.html'
    context_object_name = 'objects'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(titulo__icontains=query)
        orderby = self.request.GET.get('orderby','-pub_date')  
        return queryset.order_by(orderby)
    
class UploadView(CreateView):
    model = Video
    template_name = 'modelo/upload.html'
    fields = ['titulo','descricao','video','thumbnail']
    success_url = reverse_lazy('perfil')

class DeleteView(DeleteView):
    model = Video
    success_url = reverse_lazy('perfil')

class UpdateView(UpdateView):
    model = Video
    fields = ['titulo','descricao', 'thumbnail']
    template_name = 'modelo/update.html'
    success_url = '/perfil/'

class VideoView(ListView):
    model = Video
    template_name = 'modelo/video.html'
    context_object_name = 'Video'



