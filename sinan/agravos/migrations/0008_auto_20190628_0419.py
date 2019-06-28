# Generated by Django 2.2.1 on 2019-06-28 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agravos', '0007_auto_20190628_0410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exames',
            name='nome',
        ),
        migrations.AddField(
            model_name='exames',
            name='descricao',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='exames',
            name='tipo_de_exame',
            field=models.CharField(choices=[('CHIKUNGUNYA', 'Sorologia(IgM) Chikungunya'), ('PRNT', 'Exame PRNT'), ('DENGUE', 'Sorologia Dengue'), ('NS1', 'Exame NS1'), ('TR_PCR', 'RT-PCR')], default=1, max_length=50),
            preserve_default=False,
        ),
    ]
