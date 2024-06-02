from django.urls import path
from .views import HomeView, PerfilView

urlpatterns = [
 path('home/', HomeView.as_view(), name='home'),
 path('perfil/', PerfilView.as_view(), name='perfil'),
]