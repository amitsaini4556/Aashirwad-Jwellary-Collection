# Generated by Django 3.0.8 on 2020-07-16 05:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_reviewdatabase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewdatabase',
            name='time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 7, 16, 5, 42, 18, 474944, tzinfo=utc)),
        ),
    ]