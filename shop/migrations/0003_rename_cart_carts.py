# Generated by Django 5.0.6 on 2024-06-13 05:30

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_cart'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cart',
            new_name='Carts',
        ),
    ]
