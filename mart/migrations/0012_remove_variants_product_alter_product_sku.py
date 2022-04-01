# Generated by Django 4.0.3 on 2022-03-25 07:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0011_imagesoption_rename_colorsoptions_colorsoption_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variants',
            name='product',
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.UUIDField(default=uuid.UUID('5912e35a-be18-40d2-b01d-049876780bd0')),
        ),
    ]