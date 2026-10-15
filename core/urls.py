from django.urls import path
from . import views

urlpatterns = [
    path('projetos/', views.lista_projetos, name='lista_projetos'),
    path('projetos/<int:id>/editar/', views.editar_projeto, name='editar_projeto'),
    path('projetos/<int:id>/excluir/', views.excluir_projeto, name='excluir_projeto'),
]