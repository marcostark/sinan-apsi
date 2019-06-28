# Generated by Django 2.2.1 on 2019-06-28 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agravos', '0006_remove_notificaodengue_exames'),
    ]

    operations = [
        migrations.AddField(
            model_name='exames',
            name='exames',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='agravos.NotificaoDengue'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agravos.NotificaoDengue'),
        ),
    ]
