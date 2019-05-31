from django.db import models


class Endereco(models.Model):
    estado = models.CharField(max_length=80)
    cidade = models.CharField(max_length=255)
    bairro = models.CharField(max_length=500)
    rua = models.CharField(max_length=500)
    numero = models.IntegerField()
    cep = models.CharField(max_length=9, blank=True, null=True)

    def __str__(self):
        return "%s, %s, %s, %s - %s " % (self.rua, self.numero, self.bairro, self.cidade, self.estado)


class Pessoa(models.Model):
    SEXO_CHOICE = (
        ('HOMEM', 'Homem'),
        ('MULHER', 'Mulher')
    )
    nome_completo = models.CharField(blank=True, max_length=500)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE, null=True, blank=True,
                                    related_name='usuario_endereco', unique=True)

    telefone = models.CharField(max_length=50, blank=False, null=False)
    sexo = models.CharField(max_length=50, choices=SEXO_CHOICE, blank=True, null=True)


    def __str__(self):
        return self.nome_completo
