# Generated by Django 5.1.2 on 2024-11-11 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_order_shipping_charges'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_on',
            field=models.DateField(auto_now_add=True),
        ),
    ]