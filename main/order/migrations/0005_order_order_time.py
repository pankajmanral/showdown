# Generated by Django 5.1.2 on 2024-11-12 17:14

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_orderdetails_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_time',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
