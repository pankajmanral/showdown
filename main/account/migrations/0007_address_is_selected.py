# Generated by Django 5.1.2 on 2024-11-13 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_customer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='is_selected',
            field=models.BooleanField(default=False),
        ),
    ]
