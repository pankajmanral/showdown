# Generated by Django 5.1.2 on 2024-11-02 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='phoneNumber',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
