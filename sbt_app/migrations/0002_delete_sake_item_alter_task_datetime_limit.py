# Generated by Django 5.0.1 on 2024-02-19 10:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sbt_app', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='sake_item',
        ),
        migrations.AlterField(
            model_name='task',
            name='datetime_limit',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 19, 19, 0)),
        ),
    ]