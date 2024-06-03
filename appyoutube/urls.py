from django.urls import path
from .views import HomeView, PerfilView, ConsultaView, OrdenacaoView

urlpatterns = [
 path('home/', HomeView.as_view(), name='home'),
 path('perfil/', PerfilView.as_view(), name='perfil'),
 path('pesquisa/', ConsultaView.as_view(), name='pesquisa'),
 path('ordenar/', OrdenacaoView.as_view(), name='ordenacao')
]