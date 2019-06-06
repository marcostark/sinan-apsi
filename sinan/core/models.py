from django.db import models

class Estado(models.Model):
    nome = models.CharField(max_length=80)
    codigo_ibge = models.CharField(max_length=80)

class Cidade(models.Model):
    nome = models.CharField(max_length=80)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=True, blank=True,
                                    related_name='cidade_estado' )
    codigo_ibge = models.CharField(max_length=80)

class Endereco(models.Model):
    cidade = models.ForeignKey(Estado, on_delete=models.CASCADE, null=True, blank=True,
                               related_name='estado_cidade')
    bairro = models.CharField(max_length=500)
    rua = models.CharField(max_length=500)
    numero = models.IntegerField()
    cep = models.CharField(max_length=9, blank=True, null=True)


    def __str__(self):
        return "%s, %s, %s, %s - %s " % (self.rua, self.numero, self.bairro, self.cidade, self.estado)


class Paciente(models.Model):
    SEXO_CHOICE = (
        ('MASCULINO', 'Masculino'),
        ('FEMININO', 'Feminino'),
        ('IGNORADO', 'Ignorado'),
    )

    RACA_CHOICE = (
        ('NEGRA', 'Negra'),
        ('BRANCA', 'Branca'),
        ('PARDA', 'Parda'),
        ('INDIGENA', 'Indigena'),
    )

    nome_completo = models.CharField(blank=True, max_length=500)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True, blank=True,
                                    related_name='usuario_endereco', unique=True)

    telefone = models.CharField(max_length=50, blank=False, null=False)
    sexo = models.CharField(max_length=50, choices=SEXO_CHOICE, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    raca = models.CharField(max_length=50, choices=RACA_CHOICE, blank=True, null=True)


    def __str__(self):
        return self.nome_completo


class Unidade_de_Saude(models.Model):
    pass


