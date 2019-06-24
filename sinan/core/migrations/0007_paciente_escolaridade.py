# Generated by Django 2.2.1 on 2019-06-24 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20190624_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='escolaridade',
            field=models.CharField(blank=True, choices=[('FUNDAMENTAL INCOMPLETO', 'Ensino Fundamental Incompleto'), ('FUNDAMENTAL COMPLETO', 'Ensino Fundamental Completo'), ('ENSINO_MEDIO INCOMPLETO', 'Ensino Médio Incompleto'), ('ENSINO MEDIO COMPLETO', 'Ensino Médio Completo'), ('SUPERIOR INCOMPLETO', 'Educação Superior Incompleto'), ('SUPERIOR COMPLETO', 'Educação Superior Completa'), ('IGNORADO', 'Ignorado'), ('NÃO SE APLICA', 'Não se aplica')], max_length=50, null=True),
        ),
    ]
