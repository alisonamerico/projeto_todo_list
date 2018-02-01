# Generated by Django 2.0.1 on 2018-01-30 23:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('created_date', models.DateTimeField(default=datetime.datetime.now)),
                ('priority', models.IntegerField(choices=[(1, 'Low'), (2, 'Normal'), (3, 'High')], default=2)),
                ('completed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-priority', 'title'],
            },
        ),
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['title']},
        ),
        migrations.RemoveField(
            model_name='todo',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='text',
        ),
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(max_length=250, unique=True),
        ),
        migrations.AddField(
            model_name='item',
            name='todo_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Todo'),
        ),
    ]