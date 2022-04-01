# Generated by Django 4.0.3 on 2022-03-25 05:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0008_remove_sn_sub_id_remove_genre_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='cat',
            new_name='genre',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='type',
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.UUIDField(default=uuid.UUID('5b1ca43c-9324-4eb7-9b81-6a9fde320442')),
        ),
    ]