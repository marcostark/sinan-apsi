# Generated by Django 2.2.1 on 2019-06-28 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dengue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agravo', models.CharField(choices=[('Hanseniase', 'Hanseniase'), ('Dengue', 'Dengue'), ('Tuberculose', 'Tuberculose')], default='Dengue', max_length=100)),
                ('data_notificacao', models.DateTimeField(blank=True, null=True)),
                ('data_primeiros_sintomas', models.DateTimeField()),
                ('data_diagnostico', models.DateField(blank=True, null=True)),
                ('cidade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agravo_dengue_cidade', to='core.Cidade')),
                ('estado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agravo_dengue_estado', to='core.Estado')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Paciente')),
                ('unidade_de_saude', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agravo_dengue_usf', to='core.Unidade_de_Saude')),
            ],
            options={
                'verbose_name': 'Agravo Dengue',
                'verbose_name_plural': 'Agravos Dengue',
            },
        ),
        migrations.CreateModel(
            name='Doencas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Doença',
                'verbose_name_plural': 'Doenças',
            },
        ),
        migrations.CreateModel(
            name='Sintomas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Sintoma',
                'verbose_name_plural': 'Sintomas',
            },
        ),
        migrations.CreateModel(
            name='Tuberculose',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agravo', models.CharField(choices=[('Hanseniase', 'Hanseniase'), ('Dengue', 'Dengue'), ('Tuberculose', 'Tuberculose')], default='Tuberculose', max_length=100)),
                ('data_notificacao', models.DateField(blank=True, null=True)),
                ('data_diagnostico', models.DateField(blank=True, null=True)),
                ('cidade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agravo_cidade', to='core.Cidade')),
                ('estado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agravo_estado', to='core.Estado')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Paciente')),
                ('unidade_de_saude', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agravo_usf', to='core.Unidade_de_Saude')),
            ],
            options={
                'verbose_name': 'Agravo Tuberculose',
                'verbose_name_plural': 'Agravos de Tuberculose',
            },
        ),
        migrations.CreateModel(
            name='NotificaoDengue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isolamento', models.CharField(choices=[('POSITIVO', 'POSITIVO'), ('NEGATIVO', 'NEGATIVO'), ('INCOCLUSIVO', 'Incoclusivo'), ('NAO REALIZADO', 'Não realizado')], max_length=50)),
                ('sorotipo', models.CharField(choices=[('DENV 1', 'DENV 1'), ('DENV 2', 'DENV 2'), ('DENV 3', 'DENV 3'), ('DENV 4', 'DENV 4')], max_length=50)),
                ('histopatologia', models.CharField(choices=[('COMPATIVEL', 'Compativel'), ('INCOMPATIVEL', 'Incompativel'), ('INCONCLUSIVO', 'Inconclusivo'), ('NÃO REALIZADO', 'Não Realizado')], max_length=50)),
                ('imunohistoquimica', models.CharField(choices=[('POSITIVO', 'POSITIVO'), ('NEGATIVO', 'NEGATIVO'), ('INCOCLUSIVO', 'Incoclusivo'), ('NAO REALIZADO', 'Não realizado')], max_length=50)),
                ('agravo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agravos.Dengue')),
                ('doencas', models.ManyToManyField(to='agravos.Doencas')),
                ('sinais_clinicos', models.ManyToManyField(to='agravos.Sintomas')),
            ],
            options={
                'verbose_name': 'Notificação Dengue',
                'verbose_name_plural': 'Notificações de Dengue',
            },
        ),
        migrations.CreateModel(
            name='NotificacaoTuberculose',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ocupacao', models.CharField(max_length=100)),
                ('tipo_de_entrada', models.CharField(choices=[('NOVO', 'novo'), ('RECIDIVA', 'recidiva'), ('REINGRESSO', 'reingresso'), ('DESCONHECIDO', 'desconhecido'), ('TRANSFERENCIA', 'transaferencia')], max_length=50)),
                ('institucionalizado', models.CharField(choices=[('NÃO', 'Não'), ('PRESIDIO', 'Presidio'), ('ASILO', 'Asilo'), ('ORFANATO', 'Orfanato'), ('HOSP_PSIQUIATRICO', 'Hospital Psiquiatrico'), ('OUTROS', 'Outros'), ('IGNORADO', 'Ignorado')], max_length=50)),
                ('raiz_x', models.CharField(choices=[('SUSPEITO', 'Suspeito'), ('NORMAL', 'Normal'), ('OUTRA', 'Outra'), ('NÃO_REALIZADO', 'Não Realizado')], max_length=50)),
                ('teste_tuberculinico', models.CharField(choices=[('NÃO_REATOR', 'Não Reator '), ('REATOR FRACO', 'Reator Fraco'), ('REATOR FORTE', 'Reator Forte'), ('NÃO_REALIZADO', 'Não Realizado')], max_length=50)),
                ('forma', models.CharField(choices=[('PULMONAR', 'Pulmonar'), ('EXTRAPULMONAR', 'Extrapulmonar'), ('PULMONAR', 'Pulmonar'), ('PULMONAR_EXTRAPULMONAR', 'Pulmonar + Extrapulonar')], max_length=50)),
                ('se_extrapulmonar', models.CharField(choices=[('PLEURAL', 'Pleural'), ('GRANG_PERIF', 'Grang. Perf.'), ('GENITURINARIA', 'Geniturinaria'), ('OSSEA', 'Osséa'), ('OCULAR', 'Ocular'), ('MILIAR', 'Miliar'), ('MENINGOENCEFALICO', 'Meningoencefálico'), ('CUTANEA', 'Cutanêa'), ('LARINGEA', 'Latringêa'), ('OCULTA', 'Oculta')], max_length=50)),
                ('agravos_associados', models.CharField(choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('IGNORADO', 'Ignorado'), ('AIDS', 'Aids'), ('ALCOOLISMO', 'Alcoolismo'), ('DIABETES', 'Diabetes'), ('DOENCAO_MENTAL', 'Doença Mental'), ('OUTROS', 'Outros')], max_length=50)),
                ('basiloscopia', models.CharField(choices=[('POSITIVA', 'Positiva'), ('NEGATIVA', 'Negativa')], max_length=50)),
                ('basiloscopia_outro_material', models.CharField(choices=[('POSITIVA', 'Positiva'), ('NEGATIVA', 'Negativa'), ('NÃO REALIZADA', 'Não Realizada')], max_length=50)),
                ('cultura_de_escarro', models.CharField(choices=[('POSITIVA', 'Positiva'), ('NEGATIVA', 'Negativa'), ('ANDAMENTO', 'Andamento'), ('NÃO REALIZADA', 'Não Realizada')], max_length=50)),
                ('cultura_de_outro_material', models.CharField(choices=[('POSITIVA', 'Positiva'), ('NEGATIVA', 'Negativa'), ('ANDAMENTO', 'Andamento'), ('NÃO REALIZADA', 'Não Realizada')], max_length=50)),
                ('hiv', models.CharField(choices=[('POSITIVA', 'Positiva'), ('NEGATIVA', 'Negativa'), ('ANDAMENTO', 'Andamento'), ('NÃO REALIZADA', 'Não Realizada')], max_length=50)),
                ('histopatologia', models.CharField(choices=[('BAAR POSITIVO', 'Baar Positiva'), ('SUGESTIVO TB', 'Sugestiva TB'), ('NÃO SUGESTIVO TB', 'Não Sugestiva TB'), ('ANDAMENTO', 'Não Andamento'), ('NÃO REALIZADA', 'Não Realizada')], max_length=50)),
                ('inicio_tratamento', models.DateField()),
                ('drogas', models.CharField(choices=[('RIFAMPICINA', 'Rifamicina'), ('ISONIAZIDA', 'Isoniazida'), ('ETAMBUTOL', 'Etambutol'), ('ESTREPTOMICINA', 'Estreptomicina')], max_length=50)),
                ('tratamento_supervisionado', models.CharField(choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('IGNORADO', 'Ignorado')], max_length=50)),
                ('contatos_registados', models.IntegerField()),
                ('doenca_relacionada_ao_trabalho', models.CharField(choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('IGNORADO', 'Ignorado')], max_length=50)),
                ('tipo_agravo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agravos.Tuberculose')),
                ('unidade_de_saude', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Unidade_de_Saude')),
            ],
            options={
                'verbose_name': 'Notificação de Tuberculose',
                'verbose_name_plural': 'Notificações de Tuberculose',
            },
        ),
        migrations.CreateModel(
            name='NotificacaoHanseniese',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agravo', models.CharField(choices=[('Hanseniase', 'Hanseniase'), ('Dengue', 'Dengue'), ('Tuberculose', 'Tuberculose')], default='Hanseniese', max_length=100)),
                ('data_notificacao', models.DateField(blank=True, null=True)),
                ('data_diagnostico', models.DateField(blank=True, null=True)),
                ('numero_lesoes', models.IntegerField()),
                ('forma_clinica', models.CharField(choices=[('I', 'I'), ('T', 'T'), ('D', 'D'), ('V', 'V'), ('NAO CLASSIFICADO', 'Não Classificado')], max_length=50)),
                ('classificacao_operacional', models.CharField(choices=[('PB', 'PB'), ('MB', 'MB')], max_length=50)),
                ('num_nervos_afetados', models.IntegerField()),
                ('grau_incapacidade', models.CharField(choices=[('GRAU ZERO', 'Grau Zero'), ('GRAU I', 'Grau I'), ('GRAU II', 'Grau II'), ('GRAU III', 'Grau III'), ('NAO AVALIADO', 'Não Avaliado')], max_length=50)),
                ('modo_de_entrada', models.CharField(choices=[('NOVO', 'Caso Novo'), ('TRANSF MUNICIPIO', 'Transferência do mesmo municipio'), ('TRANSF OUTRO MUNICIPIO', 'Transferência outro municipio'), ('TRANSF  UF', 'Transferência do outro Estado'), ('OUTRO PAIS', 'Não Transferência do outro País'), ('OUTROS', 'Outros Reingressos'), ('RECIDIVA', 'Recidiva'), ('IGNORADO', 'Ignorado')], max_length=50)),
                ('modo_de_deteccao', models.CharField(choices=[('ENCAMINHAMENTO', 'Encaminhamento'), ('ESPONTANEA', 'Demanda Espontânea'), ('COLETIVIDADE', 'Exame de Coletividade'), ('CONTATOS', 'Exame de Contatos'), ('OUTROS', 'Outros Modos'), ('IGNORADO', 'Ignorado')], max_length=50)),
                ('basiloscopia', models.CharField(choices=[('POSITIVA', 'Positiva'), ('NEGATIVA', 'Negativa'), ('NAO_REALIZADA', 'Não Realizada'), ('IGNORADO', 'Ignorado')], max_length=50)),
                ('inicio_tratamento', models.DateField()),
                ('contatos_registados', models.IntegerField()),
                ('cidade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='not_hanseniese_cidade', to='core.Cidade')),
                ('estado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='not_hanseniese_estado', to='core.Estado')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Paciente')),
                ('unidade_de_saude', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Unidade_de_Saude')),
            ],
            options={
                'verbose_name': 'Agravo Hanseniese',
                'verbose_name_plural': 'Agravo Hanseniese',
            },
        ),
        migrations.CreateModel(
            name='Exames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_de_exame', models.CharField(choices=[('CHIKUNGUNYA', 'Sorologia(IgM) Chikungunya'), ('PRNT', 'Exame PRNT'), ('DENGUE', 'Sorologia Dengue'), ('NS1', 'Exame NS1'), ('TR_PCR', 'RT-PCR')], max_length=50)),
                ('descricao', models.CharField(blank=True, max_length=250, null=True)),
                ('primeira_coleta', models.DateField()),
                ('segunda_coleta', models.DateField(blank=True, null=True)),
                ('resul_primeira_coleta', models.CharField(choices=[('POSITIVO', 'POSITIVO'), ('NEGATIVO', 'NEGATIVO'), ('INCOCLUSIVO', 'Incoclusivo'), ('NAO REALIZADO', 'Não realizado')], max_length=50)),
                ('resul_segunda_coleta', models.CharField(choices=[('POSITIVO', 'POSITIVO'), ('NEGATIVO', 'NEGATIVO'), ('INCOCLUSIVO', 'Incoclusivo'), ('NAO REALIZADO', 'Não realizado')], max_length=50)),
                ('exames', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agravos.Dengue')),
            ],
            options={
                'verbose_name': 'Exame',
                'verbose_name_plural': 'Exames',
            },
        ),
    ]
