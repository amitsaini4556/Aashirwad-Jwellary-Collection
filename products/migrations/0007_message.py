# Generated by Django 3.0.8 on 2020-07-12 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20200712_0436'),
    ]

    operations = [
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.IntegerField(max_length=15)),
                ('message', models.TextField()),
            ],
        ),
    ]
