from django.db import models

class Estado(models.Model):
    nome = models.CharField(max_length=80)
    codigo_ibge = models.CharField(max_length=80)

    def __str__(self):
        return self.nome

class Cidade(models.Model):
    nome = models.CharField(max_length=80)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE,
                                    related_name='cidade_estado' )
    codigo_ibge = models.CharField(max_length=80)

    def __str__(self):
        return self.nome

class Endereco(models.Model):
    cidade = models.ForeignKey(Estado, on_delete=models.CASCADE,
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

    GESTANTE = (
        ('1° TRIMESTE', '1° Trimestre '),
        ('2° TRIMESTE', '2° Trimestre'),
        ('3° TRIMESTE', '3° Trimestre'),
        ('IDADE GESTACIONAL IGNORADA', 'Idade Gestacional Ignorada'),
        ('NÃO', 'Não'),
        ('NÃO SE APLICA', 'Não se Aplica'),
        ('IGNORADO', 'Ignorado'),
    )

    ESCOLARIDADE = (
        ('FUNDAMENTAL INCOMPLETO', 'Ensino Fundamental Incompleto'),
        ('FUNDAMENTAL COMPLETO', 'Ensino Fundamental Completo'),
        ('ENSINO_MEDIO INCOMPLETO', 'Ensino Médio Incompleto'),
        ('ENSINO MEDIO COMPLETO', 'Ensino Médio Completo'),
        ('SUPERIOR INCOMPLETO', 'Educação Superior Incompleto'),
        ('SUPERIOR COMPLETO', 'Educação Superior Completa'),
        ('IGNORADO', 'Ignorado'),
        ('NÃO SE APLICA', 'Não se aplica'),
    )
    ZONA = (
        ('URBANA', 'Urbana'),
        ('RURAL', 'Rural'),
        ('PERIURBANA', 'Periurbana'),
        ('IGNORADO', 'Ignorado'),
    )


    nome_completo = models.CharField(blank=True, max_length=500)
    # endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True, blank=True,
    #                                 related_name='usuario_endereco', unique=True)
    data_nascimento = models.DateField(blank=True, null=True)
    sexo = models.CharField(max_length=50, choices=SEXO_CHOICE)
    gestante = models.CharField(max_length=50, choices=GESTANTE)
    raca = models.CharField(max_length=50, choices=RACA_CHOICE)
    escolaridade = models.CharField(max_length=50, choices=ESCOLARIDADE)
    numero_carta_sus = models.CharField(max_length=15)
    nome_da_mae = models.CharField(blank=True, max_length=500)
    cidade =  models.ForeignKey(Cidade, on_delete=models.CASCADE,
                                related_name='paciente_cidade')
    distrito = models.CharField(max_length=500)
    bairro = models.CharField(max_length=500)
    rua = models.CharField(max_length=500)
    numero = models.IntegerField()
    cep = models.CharField(max_length=9)
    ponto_referencia = models.CharField(max_length=500)
    latitude = models.CharField(max_length= 50,blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    telefone = models.CharField(max_length=50)
    zona = models.CharField(max_length=50, choices=ZONA)

    def __str__(self):
        return self.nome


    def __str__(self):
        return self.nome_completo


class Unidade_de_Saude(models.Model):
    nome = models.CharField(max_length=80)
    codigo = models.CharField(max_length=10)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE,
                               related_name='unidade_cidade')
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE,
                               related_name='unidade_estado')
    pais = models.CharField(blank=True, max_length=500)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Unidade de Saúde'
        verbose_name_plural = 'Unidades de Saúde'

