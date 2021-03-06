from django.db import models
from core.models import Cidade, Estado, Unidade_de_Saude
from core.models import Paciente

AGRAVO = (
    ('Hanseniase', 'Hanseniase'),
    ('Dengue', 'Dengue'),
    ('Tuberculose', 'Tuberculose'),
)

TIPO_DE_ENTRADA= (
    ('NOVO', 'novo'),
    ('RECIDIVA', 'recidiva'),
    ('REINGRESSO', 'reingresso'),
    ('DESCONHECIDO', 'desconhecido'),
    ('TRANSFERENCIA', 'transaferencia'),
)

INSTITUCIONALIZADO= (
    ('NÃO', 'Não'),
    ('PRESIDIO', 'Presidio'),
    ('ASILO', 'Asilo'),
    ('ORFANATO', 'Orfanato'),
    ('HOSP_PSIQUIATRICO', 'Hospital Psiquiatrico'),
    ('OUTROS', 'Outros'),
    ('IGNORADO', 'Ignorado'),
)

RAIO_X= (
    ('SUSPEITO', 'Suspeito'),
    ('NORMAL', 'Normal'),
    ('OUTRA', 'Outra'),
    ('NÃO_REALIZADO', 'Não Realizado'),
)

TESTE_TUBERCULINICO = (
    ('NÃO_REATOR', 'Não Reator '),
    ('REATOR FRACO', 'Reator Fraco'),
    ('REATOR FORTE', 'Reator Forte'),
    ('NÃO_REALIZADO', 'Não Realizado'),
)

FORMA = (
    ('PULMONAR', 'Pulmonar'),
    ('EXTRAPULMONAR', 'Extrapulmonar'),
    ('PULMONAR', 'Pulmonar'),
    ('PULMONAR_EXTRAPULMONAR', 'Pulmonar + Extrapulonar'),
)

SE_EXTRAPULMONAR = (
    ('PLEURAL', 'Pleural'),
    ('GRANG_PERIF', 'Grang. Perf.'),
    ('GENITURINARIA', 'Geniturinaria'),
    ('OSSEA', 'Osséa'),
    ('OCULAR', 'Ocular'),
    ('MILIAR', 'Miliar'),
    ('MENINGOENCEFALICO', 'Meningoencefálico'),
    ('CUTANEA', 'Cutanêa'),
    ('LARINGEA', 'Latringêa'),
    ('OCULTA', 'Oculta'),
)

AGRAVOS_ASSOCIADOS = (
    ('SIM', 'Sim'),
    ('NÃO', 'Não'),
    ('IGNORADO', 'Ignorado'),
    ('AIDS', 'Aids'),
    ('ALCOOLISMO', 'Alcoolismo'),
    ('DIABETES', 'Diabetes'),
    ('DOENCAO_MENTAL', 'Doença Mental'),
    ('OUTROS', 'Outros'),
)

BACILOSCOPIA = (
    ('POSITIVA', 'Positiva'),
    ('NEGATIVA', 'Negativa'),
)

OUTRA_BASICOLOSPIA= (
    ('POSITIVA', 'Positiva'),
    ('NEGATIVA', 'Negativa'),
    ('NÃO REALIZADA', 'Não Realizada'),
)

ESCARRO=(
    ('POSITIVA', 'Positiva'),
    ('NEGATIVA', 'Negativa'),
    ('ANDAMENTO', 'Andamento'),
    ('NÃO REALIZADA', 'Não Realizada'),
)

OUTRA_CULTURA= (
    ('POSITIVA', 'Positiva'),
    ('NEGATIVA', 'Negativa'),
    ('ANDAMENTO', 'Andamento'),
    ('NÃO REALIZADA', 'Não Realizada'),
)

HIV= (
    ('POSITIVA', 'Positiva'),
    ('NEGATIVA', 'Negativa'),
    ('ANDAMENTO', 'Andamento'),
    ('NÃO REALIZADA', 'Não Realizada'),
)

HISTOLOPATOLOGIA= (
    ('BAAR POSITIVO', 'Baar Positiva'),
    ('SUGESTIVO TB', 'Sugestiva TB'),
    ('NÃO SUGESTIVO TB', 'Não Sugestiva TB'),
    ('ANDAMENTO', 'Não Andamento'),
    ('NÃO REALIZADA', 'Não Realizada'),
)

DROGAS= (
    ('RIFAMPICINA', 'Rifamicina'),
    ('ISONIAZIDA', 'Isoniazida'),
    ('ETAMBUTOL', 'Etambutol'),
    ('ESTREPTOMICINA', 'Estreptomicina'),
)

TRATAMENTO_SUPERVISIONADO= (
    ('SIM', 'Sim'),
    ('NÃO', 'Não'),
    ('IGNORADO', 'Ignorado'),
)

DOENCA_TRABALHO= (
    ('SIM', 'Sim'),
    ('NÃO', 'Não'),
    ('IGNORADO', 'Ignorado'),
)

# DENGUE --------------------------------------------

SINAIS_CLINICOS = (
    ('FEBRE', 'Febre'),
    ('CEFALEIA', 'Cefaleia'),
    ('VOMITO', 'Vômito'),
    ('DOR NAS COSTAS', 'Dor nas Costas'),
    ('ARTRITE', 'Artrite'),
    ('PETEQUIAS', 'Petequias'),
    ('PROVA DO LACO', 'Prova do Laço'),
    ('MIALGIA', 'Mialgia'),
    ('EXANTEMA', 'Exantema'),
    ('NAUSEAS', 'Nauséas'),
    ('CONJUTIVITE', 'Conjutivite'),
    ('ARTRALGIA', 'Artralgia'),
    ('LEUCOPENIA', 'Leucopente'),
)

DOENCAS_PREEXISTENTES= (
    ('DIABETES', 'Diabetes'),
    ('DOENCAS HEMATOLOGICAS', 'Doencas Hametologicas'),
    ('HEPATOPATIAS', 'Hepatopatias'),
    ('DOENCA RENAL', 'Doença Renal'),
    ('HIPERTENSAO ARTERIAL', 'Hipertensão Arterial'),
    ('ACIDO-PEPTICA', 'Doença Ácido-Peptica'),
    ('AUTO-IMUNE', 'Doença Auto-Imune'),
)

RESULTADO = (
    ('POSITIVO', 'POSITIVO'),
    ('NEGATIVO', 'NEGATIVO'),
    ('INCOCLUSIVO', 'Incoclusivo'),
    ('NAO REALIZADO', 'Não realizado'),
)

SOROTIPO= (
    ('DENV 1', 'DENV 1'),
    ('DENV 2', 'DENV 2'),
    ('DENV 3', 'DENV 3'),
    ('DENV 4', 'DENV 4'),
)

HISTOPATOLOGIA= (
    ('COMPATIVEL', 'Compativel'),
    ('INCOMPATIVEL', 'Incompativel'),
    ('INCONCLUSIVO', 'Inconclusivo'),
    ('NÃO REALIZADO', 'Não Realizado'),
)


# HANSENIESE --------------------------------------------

FORMA_CLINICA = (
    ('I', 'I'),
    ('T', 'T'),
    ('D', 'D'),
    ('V', 'V'),
    ('NAO CLASSIFICADO', 'Não Classificado'),
)

CLASSIFICACAO_OPERACIONAL = (
    ('PB', 'PB'),
    ('MB', 'MB'),
)

GRAU_INCAPACIDADE = (
    ('GRAU ZERO', 'Grau Zero'),
    ('GRAU I', 'Grau I'),
    ('GRAU II', 'Grau II'),
    ('GRAU III', 'Grau III'),
    ('NAO AVALIADO', 'Não Avaliado'),
)

MODO_ENTRADA = (
    ('NOVO', 'Caso Novo'),
    ('TRANSF MUNICIPIO', 'Transferência do mesmo municipio'),
    ('TRANSF OUTRO MUNICIPIO', 'Transferência outro municipio'),
    ('TRANSF  UF', 'Transferência do outro Estado'),
    ('OUTRO PAIS', 'Não Transferência do outro País'),
    ('OUTROS', 'Outros Reingressos'),
    ('RECIDIVA', 'Recidiva'),
    ('IGNORADO', 'Ignorado'),
)

DETECCAO_CASO= (
    ('ENCAMINHAMENTO', 'Encaminhamento'),
    ('ESPONTANEA', 'Demanda Espontânea'),
    ('COLETIVIDADE', 'Exame de Coletividade'),
    ('CONTATOS', 'Exame de Contatos'),
    ('OUTROS', 'Outros Modos'),
    ('IGNORADO', 'Ignorado'),
)

HAN_BACILOSCOPIA= (
    ('POSITIVA', 'Positiva'),
    ('NEGATIVA', 'Negativa'),
    ('NAO_REALIZADA', 'Não Realizada'),
    ('IGNORADO', 'Ignorado'),
)

ESQUEMA_TERAPEUTICO= (
    ('SEIS', 'PQT/PB/6 doses'),
    ('DOZE', 'PQT/MB/12 doses'),
    ('OUTROS', 'Não Realizada'),
)

TIPOS_EXAMES = (
    ('CHIKUNGUNYA', 'Sorologia(IgM) Chikungunya'),
    ('PRNT', 'Exame PRNT'),
    ('DENGUE', 'Sorologia Dengue'),
    ('NS1', 'Exame NS1'),
    ('TR_PCR', 'RT-PCR'),
)

class Tuberculose(models.Model):
    agravo = models.CharField(choices=AGRAVO, max_length=100, default='Tuberculose')
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    #notificacao = models.ForeignKey(NotificacaoTuberculose, on_delete=models.CASCADE)
    data_notificacao = models.DateField(blank=True, null=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=True, blank=True, related_name='agravo_estado')
    cidade = models.ForeignKey(Cidade, on_delete= models.CASCADE, null=True, blank=True, related_name='agravo_cidade')
    unidade_de_saude = models.ForeignKey(Unidade_de_Saude, on_delete=models.CASCADE, null=True, blank=True, related_name='agravo_usf')
    data_diagnostico = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = 'Agravo Tuberculose'
        verbose_name_plural = 'Agravos de Tuberculose'

    def __str__(self):
        return self.agravo


class NotificacaoTuberculose(models.Model):
    tipo_agravo = models.ForeignKey(Tuberculose, on_delete=models.CASCADE)
    ocupacao = models.CharField(max_length=100)
    tipo_de_entrada = models.CharField(max_length=50, choices=TIPO_DE_ENTRADA)
    institucionalizado = models.CharField(max_length=50, choices=INSTITUCIONALIZADO)
    raiz_x = models.CharField(max_length=50, choices=RAIO_X)
    teste_tuberculinico = models.CharField(max_length=50, choices=TESTE_TUBERCULINICO)
    forma = models.CharField(max_length=50, choices=FORMA)
    se_extrapulmonar = models.CharField(max_length=50, choices=SE_EXTRAPULMONAR)
    agravos_associados = models.CharField(max_length=50, choices=AGRAVOS_ASSOCIADOS)
    basiloscopia = models.CharField(max_length=50, choices=BACILOSCOPIA)
    basiloscopia_outro_material = models.CharField(max_length=50, choices=OUTRA_BASICOLOSPIA)
    cultura_de_escarro = models.CharField(max_length=50, choices=ESCARRO)
    cultura_de_outro_material = models.CharField(max_length=50, choices=OUTRA_CULTURA)
    hiv = models.CharField(max_length=50, choices=HIV)
    histopatologia = models.CharField(max_length=50, choices=HISTOLOPATOLOGIA)
    inicio_tratamento = models.DateField()
    drogas =  models.CharField(max_length=50, choices=DROGAS)
    tratamento_supervisionado = models.CharField(max_length=50, choices=TRATAMENTO_SUPERVISIONADO)
    contatos_registados = models.IntegerField()
    doenca_relacionada_ao_trabalho= models.CharField(max_length=50, choices=DOENCA_TRABALHO)
    unidade_de_saude = models.ForeignKey(Unidade_de_Saude, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Notificação de Tuberculose'
        verbose_name_plural = 'Notificações de Tuberculose'

    def __str__(self):
        return self.tipo_agravo.agravo


# DENGUE ---------------------------------------------------------------------------------------------------------------
class Sintomas(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Sintoma'
        verbose_name_plural = 'Sintomas'

    def __str__(self):
        return self.nome

class Doencas(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Doença'
        verbose_name_plural = 'Doenças'

    def __str__(self):
        return self.nome


class Dengue(models.Model):
    agravo = models.CharField(choices=AGRAVO, max_length=100, default='Dengue')
    data_notificacao = models.DateTimeField(blank=True, null=True)
    data_primeiros_sintomas = models.DateTimeField()
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=True, blank=True, related_name='agravo_dengue_estado')
    cidade = models.ForeignKey(Cidade, on_delete= models.CASCADE, null=True, blank=True, related_name='agravo_dengue_cidade')
    unidade_de_saude = models.ForeignKey(Unidade_de_Saude, on_delete=models.CASCADE, null=True, blank=True, related_name='agravo_dengue_usf')
    data_diagnostico = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = 'Agravo Dengue'
        verbose_name_plural = 'Agravos Dengue'

    def __str__(self):
        return self.agravo


class NotificaoDengue(models.Model):
    agravo = models.ForeignKey(Dengue, on_delete=models.CASCADE)
    sinais_clinicos = models.ManyToManyField(Sintomas)
    doencas = models.ManyToManyField(Doencas)
    isolamento = models.CharField(max_length=50, choices=RESULTADO)
    sorotipo = models.CharField(max_length=50, choices=SOROTIPO)
    histopatologia = models.CharField(max_length=50, choices=HISTOPATOLOGIA)
    imunohistoquimica = models.CharField(max_length=50, choices=RESULTADO)

    class Meta:
        verbose_name = 'Notificação Dengue'
        verbose_name_plural = 'Notificações de Dengue'

    def __str__(self):
        return self.agravo.agravo


class Exames(models.Model):
    tipo_de_exame = models.CharField(max_length=50, choices=TIPOS_EXAMES)
    descricao = models.CharField(max_length=250, blank=True, null=True)
    exames = models.ForeignKey(Dengue, on_delete=models.CASCADE)
    primeira_coleta = models.DateField()
    segunda_coleta = models.DateField(blank=True, null=True)
    resul_primeira_coleta = models.CharField(max_length=50, choices=RESULTADO)
    resul_segunda_coleta = models.CharField(max_length=50, choices=RESULTADO)

    class Meta:
        verbose_name = 'Exame'
        verbose_name_plural = 'Exames'

    def __str__(self):
        return self.tipo_de_exame

# HANSENIESE -----------------------------------------------------------------------------------------------------------

class NotificacaoHanseniese(models.Model):
    agravo = models.CharField(choices=AGRAVO, max_length=100, default='Hanseniese')
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    data_notificacao = models.DateField(blank=True, null=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=True, blank=True, related_name='not_hanseniese_estado')
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, null=True, blank=True, related_name='not_hanseniese_cidade')
    unidade_de_saude = models.ForeignKey(Unidade_de_Saude, on_delete=models.CASCADE, null=True, blank=True,
                                         related_name='not_hanseniese_usf')
    data_diagnostico = models.DateField(blank=True, null=True)
    numero_lesoes = models.IntegerField()
    forma_clinica = models.CharField(max_length=50, choices=FORMA_CLINICA)
    classificacao_operacional = models.CharField(max_length=50, choices=CLASSIFICACAO_OPERACIONAL)
    num_nervos_afetados = models.IntegerField()
    grau_incapacidade = models.CharField(max_length=50, choices=GRAU_INCAPACIDADE)
    modo_de_entrada = models.CharField(max_length=50, choices=MODO_ENTRADA)
    modo_de_deteccao = models.CharField(max_length=50, choices=DETECCAO_CASO)
    basiloscopia = models.CharField(max_length=50, choices=HAN_BACILOSCOPIA)
    inicio_tratamento = models.DateField()
    contatos_registados = models.IntegerField()
    unidade_de_saude = models.ForeignKey(Unidade_de_Saude, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Agravo Hanseniese'
        verbose_name_plural = 'Agravo Hanseniese'

    def __str__(self):
        return self.paciente.nome_completo
