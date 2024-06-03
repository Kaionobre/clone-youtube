from django.urls import path
from django.contrib.auth import views as auth_views

from .views import HomeView, PerfilView, ConsultaView, OrdenacaoView, UploadView

urlpatterns = [
 path('home/', HomeView.as_view(), name='home'),
 path('perfil/', PerfilView.as_view(), name='perfil'),
 path('pesquisa/', ConsultaView.as_view(), name='pesquisa'),
 path('ordenar/', OrdenacaoView.as_view(), name='ordenacao'),
 path('upload/', UploadView.as_view(), name='upload'),
 path('logout/', auth_views.LogoutView.as_view(next_page='/home'), name='logout'),

]