from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    data_nascimento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        input_formats=['%Y-%m-%d']
    )

    cpf = forms.CharField(
        max_length=14,
        widget=forms.TextInput(attrs={'placeholder': '000.000.000-00'})
    )

    class Meta:
        model = Cliente
        fields = ['nome', 'data_nascimento', 'cpf', 'email']

    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        numeros = ''.join(filter(str.isdigit, cpf))

        if len(numeros) != 11:
            raise forms.ValidationError("CPF deve conter exatamente 11 dígitos.")
        return f"{numeros[:3]}.{numeros[3:6]}.{numeros[6:9]}-{numeros[9:]}"
