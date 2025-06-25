from django import forms
from .models import Assinatura
from clientes.models import Cliente

class AssinaturaForm(forms.ModelForm):
    clientes = forms.ModelMultipleChoiceField(
        queryset=Cliente.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Assinatura
        fields = ['nome', 'mensalidade', 'clientes']
