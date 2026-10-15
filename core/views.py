from django.shortcuts import render, redirect

# Create your views here.

from .models import Projeto
from .forms import ProjetoForm

def lista_projetos(request):
    projetos = Projeto.objects.all()

    if request.method == 'POST':
        form = ProjetoForm(request.POST)

        if form.is_valid():
            form.save()
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
        return redirect('lista_projetos')

    return render(request, 'core/excluir_projeto.html', {
        'projeto': projeto
    })