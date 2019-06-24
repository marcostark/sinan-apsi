# Generated by Django 2.2.1 on 2019-06-24 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20190624_1525'),
        ('agravos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipo_agravo',
            name='cidade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agravo_cidade', to='core.Cidade'),
        ),
        migrations.AddField(
            model_name='tipo_agravo',
            name='data_diagnostico',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tipo_agravo',
            name='data_notificacao',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tipo_agravo',
            name='estado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agravo_estado', to='core.Estado'),
        ),
        migrations.AddField(
            model_name='tipo_agravo',
            name='unidade_de_saude',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agravo_cidade', to='core.Unidade_de_Saude'),
        ),
    ]