from django.shortcuts import render, redirect, get_object_or_404
from .models import Assinatura
from .forms import AssinaturaForm

def lista_assinaturas(request):
    assinaturas = Assinatura.objects.all()
    return render(request, 'assinaturas/lista_assinaturas.html', {'assinaturas': assinaturas})

def nova_assinatura(request):
    if request.method == 'POST':
        form = AssinaturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_assinaturas')
    else:
        form = AssinaturaForm()
    return render(request, 'assinaturas/nova_assinatura.html', {'form': form})

def assinatura_por_clientes(request, assinatura_id):
    assinatura = get_object_or_404(Assinatura, id=assinatura_id)
    return render(request, 'assinaturas/assinatura_por_clientes.html', {'assinatura': assinatura})
