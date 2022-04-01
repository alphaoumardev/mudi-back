# Generated by Django 4.0.3 on 2022-03-21 08:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0002_rename_name_genre_genre_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='onsale',
            field=models.CharField(blank=True, choices=[('Sale', 'Sale'), ('New', 'New')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.UUIDField(default=uuid.UUID('14aeedd3-978b-4a59-9b89-f09117c54869')),
        ),
    ]
