# Generated by Django 5.0.1 on 2024-11-05 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_product_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='address',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
