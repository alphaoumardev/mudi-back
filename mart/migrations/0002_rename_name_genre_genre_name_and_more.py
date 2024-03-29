# Generated by Django 4.0.3 on 2022-03-20 14:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genre',
            old_name='name',
            new_name='genre_name',
        ),
        migrations.RenameField(
            model_name='types',
            old_name='name',
            new_name='type_name',
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.UUIDField(default=uuid.UUID('684e8077-5733-4847-ba47-3c12661475e1')),
        ),
    ]
