from django.urls import path
from accounts.views import login, cadastro

urlpatterns = [
    path('login/', login, name='login'),
    path('cadastro/', cadastro, name='cadastro'),
]
