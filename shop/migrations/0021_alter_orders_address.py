# Generated by Django 5.0.6 on 2024-07-26 10:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0020_orders_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.shippingaddress'),
        ),
    ]
