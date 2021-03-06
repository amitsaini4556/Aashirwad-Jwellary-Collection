# Generated by Django 3.0.8 on 2020-07-17 02:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0024_auto_20200717_0754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='braceletsdatabase',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 17, 2, 29, 6, 195905, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='earingsdatabase',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 17, 2, 29, 6, 197035, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='featuredproducts',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 17, 2, 29, 6, 194140, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='jewellarydatabase',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 17, 2, 29, 6, 196359, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='reviewdatabase',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 17, 2, 29, 6, 198104, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ringsdatabase',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 17, 2, 29, 6, 194868, tzinfo=utc)),
        ),
    ]
