# Generated by Django 2.0.1 on 2018-02-03 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20180203_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.CharField(choices=[('BAIXA', 'Baixa'), ('NORMAL', 'Normal'), ('ALTA', 'Alta')], default='NORMAL', max_length=6),
        ),
    ]
