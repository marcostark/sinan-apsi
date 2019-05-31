from django.db import models

AGRAVO = (
    ('Hanseniase', 'Hanseniase'),
    ('Dengue', 'Dengue'),
    ('Tuberculose', 'Tuberculose'),
)

class Tipo_Agravo(models.Model):
    agravo = models.CharField(choices=AGRAVO, max_length=100, default='')

    class Meta:
        verbose_name = 'Tipo de Agravo'
        verbose_name_plural = 'Tipos de Agravos'

    def __str__(self):
        return self.bairro
