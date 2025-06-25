from django.db import models
from clientes.models import Cliente

class Assinatura(models.Model):
    nome = models.CharField(max_length=100)
    mensalidade = models.DecimalField(max_digits=6, decimal_places=2)
    clientes = models.ManyToManyField(Cliente)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        self.nome = self.nome.title()
        super().save(*args, **kwargs)
