# Generated by Django 5.1.2 on 2024-11-12 17:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_order_order_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_time',
            field=models.TimeField(default=datetime.time(12, 0)),
        ),
    ]
