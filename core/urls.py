from django.urls import path
from . import views

urlpatterns = [
    path('projetos/', views.lista_projetos, name='lista_projetos'),
    path('projetos/<int:id>/editar/', views.editar_projeto, name='editar_projeto'),
    path('projetos/<int:id>/excluir/', views.excluir_projeto, name='excluir_projeto'),

    path('tarefas/', views.lista_tarefas, name='lista_tarefas'),
    path('tarefas/nova/', views.criar_tarefa, name='criar_tarefa'),
    path('tarefas/<int:pk>/editar/', views.editar_tarefa, name='editar_tarefa'),
    path('tarefas/<int:pk>/excluir/', views.excluir_tarefa, name='excluir_tarefa'),

]