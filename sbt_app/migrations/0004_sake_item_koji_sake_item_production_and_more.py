# Generated by Django 5.0.1 on 2025-06-05 22:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sbt_app', '0003_sake_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='sake_item',
            name='koji',
            field=models.CharField(default='giallo', max_length=20),
        ),
        migrations.AddField(
            model_name='sake_item',
            name='production',
            field=models.CharField(default='sokujo moto', max_length=20),
        ),
        migrations.AlterField(
            model_name='task',
            name='datetime_limit',
            field=models.DateTimeField(default=datetime.datetime(2025, 6, 6, 19, 0)),
        ),
    ]
