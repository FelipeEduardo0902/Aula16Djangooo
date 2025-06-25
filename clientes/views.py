from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from assinaturas.models import Assinatura
from .forms import ClienteForm

def lista_clientes(request):
    busca = request.GET.get('busca', '')
    clientes = Cliente.objects.filter(nome__icontains=busca)
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})

def cadastro_clientes(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'clientes/cadastro_clientes.html', {'form': form})

def cliente_assinaturas(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return render(request, 'clientes/cliente_assinaturas.html', {'cliente': cliente})
