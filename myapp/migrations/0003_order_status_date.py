# Generated by Django 2.2.1 on 2019-05-28 07:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20190528_0716'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]