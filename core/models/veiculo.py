from django.db import models

from dill.temp import b


from .acessorio import Acessorio
from .cor import Cor
from .modelo import Modelo

class Veiculo(models.Model):
    ano = models.IntegerField(null=True, blank=True, default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name="veiculos", blank=True, null=True)
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculos", blank=True, null=True)
    acessorios = models.ManyToManyField(Acessorio, related_name="veiculos", blank=True)

    def __str__(self):
        return f"{self.id} - {self.modelo} {self.cor} ({self.ano})"
