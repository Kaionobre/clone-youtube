from django.urls import path
from accounts.views import LoginView, CadastroView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('cadastro/', CadastroView.as_view(), name='cadastro'),
]
