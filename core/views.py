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
