# Generated by Django 2.0.1 on 2018-02-05 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_auto_20180205_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='deadline',
            field=models.DateTimeField(default=None),
        ),
    ]