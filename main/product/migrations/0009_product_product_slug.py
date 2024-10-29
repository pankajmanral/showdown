# Generated by Django 5.1.2 on 2024-10-28 16:51

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_alter_product_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_slug',
            field=autoslug.fields.AutoSlugField(blank=True, editable=False, populate_from='product_name'),
        ),
    ]
