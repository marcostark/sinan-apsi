from django.db import models
from core.models import Cidade, Estado, Unidade_de_Saude

AGRAVO = (
    ('Hanseniase', 'Hanseniase'),
    ('Dengue', 'Dengue'),
    ('Tuberculose', 'Tuberculose'),
)

class Tipo_Agravo(models.Model):
    agravo = models.CharField(choices=AGRAVO, max_length=100, default='')
    data_notificacao = models.DateField(blank=True, null=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=True, blank=True, related_name='agravo_estado')
    cidade = models.ForeignKey(Cidade, on_delete= models.CASCADE, null=True, blank=True, related_name='agravo_cidade')
    unidade_de_saude = models.ForeignKey(Unidade_de_Saude, on_delete=models.CASCADE, null=True, blank=True, related_name='agravo_cidade')
    data_diagnostico = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = 'Tipo de Agravo'
        verbose_name_plural = 'Tipos de Agravos'

    def __str__(self):
        return self.bairro
