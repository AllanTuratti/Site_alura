from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Receita


def index(request):
    receitas =  Receita.objects.order_by('-date_receita').filter(publicado=True)

    dados = {
        'receitas' : receitas
    }

    return render(request, 'index.html', dados)

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    receita_exibir = {
        'receita' : receita
    }

    return render(request, 'receita.html', receita_exibir)

def buscar(request):

    buscar_receitas =  Receita.objects.order_by('-date_receita').filter(publicado=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if buscar:
            buscar_receitas = buscar_receitas.filter(nome_receita__icontains=nome_a_buscar)

    dados = {
        'receitas' : buscar_receitas
    }
    return render(request, 'buscar.html', dados)
