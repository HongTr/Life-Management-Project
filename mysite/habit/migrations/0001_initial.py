# Generated by Django 4.0.2 on 2022-03-18 04:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('counter', models.PositiveSmallIntegerField(default=0)),
                ('complete', models.BooleanField(default=False)),
                ('start_date', models.DateField(default=datetime.date(2022, 3, 18))),
            ],
        ),
    ]