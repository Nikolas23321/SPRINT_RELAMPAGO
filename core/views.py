from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Projeto, Tarefa
from .forms import ProjetoForm, TarefaForm


def lista_projetos(request):
    projetos = Projeto.objects.all()

    if request.method == 'POST':
        form = ProjetoForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Projeto cadastrado com sucesso!')
            return redirect('lista_projetos')
    else:
        form = ProjetoForm()

    return render(request, 'core/lista_projetos.html', {
        'projetos': projetos,
        'form': form
    })


def editar_projeto(request, id):
    projeto = Projeto.objects.get(id=id)

    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)

        if form.is_valid():
            form.save()
            messages.success(request, 'Projeto atualizado com sucesso!')
            return redirect('lista_projetos')
    else:
        form = ProjetoForm(instance=projeto)

    return render(request, 'core/editar_projeto.html', {
        'form': form,
        'projeto': projeto
    })


def excluir_projeto(request, id):
    projeto = Projeto.objects.get(id=id)

    if request.method == 'POST':
        projeto.delete()
        messages.success(request, 'Projeto excluído com sucesso!')
        return redirect('lista_projetos')

    return render(request, 'core/excluir_projeto.html', {
        'projeto': projeto
    })


def lista_tarefas(request):
    tarefas = Tarefa.objects.select_related('projeto').all()

    return render(request, 'core/lista_tarefas.html', {
        'tarefas': tarefas
    })


def criar_tarefa(request):
    form = TarefaForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Tarefa cadastrada com sucesso!')
        return redirect('lista_tarefas')

    return render(request, 'core/form_tarefa.html', {
        'form': form
    })


def editar_tarefa(request, pk):
    tarefa = Tarefa.objects.get(pk=pk)
    form = TarefaForm(request.POST or None, instance=tarefa)

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Tarefa atualizada com sucesso!')
        return redirect('lista_tarefas')

    return render(request, 'core/form_tarefa.html', {
        'form': form
    })


def excluir_tarefa(request, pk):
    tarefa = Tarefa.objects.get(pk=pk)

    if request.method == 'POST':
        tarefa.delete()
        messages.success(request, 'Tarefa excluída com sucesso!')
        return redirect('lista_tarefas')

    return render(request, 'core/excluir_tarefa.html', {
        'tarefa': tarefa
    })
