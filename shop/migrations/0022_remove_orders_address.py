# Generated by Django 5.0.6 on 2024-07-26 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0021_alter_orders_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='address',
        ),
    ]
