# Generated by Django 3.0.8 on 2020-07-17 02:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_auto_20200717_0744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='braceletsdatabase',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 17, 2, 20, 51, 551726, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='earingsdatabase',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 17, 2, 20, 51, 553320, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='featuredproducts',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 17, 2, 20, 51, 549231, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='jewellarydatabase',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 17, 2, 20, 51, 552524, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='necklessdatabase',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 17, 7, 50, 51, 550939)),
        ),
        migrations.AlterField(
            model_name='reviewdatabase',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 17, 2, 20, 51, 554921, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ringsdatabase',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 17, 2, 20, 51, 550079, tzinfo=utc)),
        ),
    ]
