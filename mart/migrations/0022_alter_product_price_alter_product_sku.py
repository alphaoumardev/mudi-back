# Generated by Django 4.0.3 on 2022-04-01 05:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0021_alter_product_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=20, max_digits=6),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.UUIDField(default=uuid.UUID('22359785-c392-40db-9679-a78adef84567')),
        ),
    ]
