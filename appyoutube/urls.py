from django.urls import path
from .views import BaseView, PerfilView

urlpatterns = [
 path('base/', BaseView.as_view(), name='home'),
 path('perfil/', PerfilView.as_view(), name='perfil'),

]