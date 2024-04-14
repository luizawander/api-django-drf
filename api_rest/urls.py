from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('profissional/', views.get_profissional, name='get_profissional'),  # Rota para obter lista de profissionais
    path('consulta/', views.get_consulta, name='get_consulta'),  # Rota para obter lista de consultas
] 