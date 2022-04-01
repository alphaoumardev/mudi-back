# Generated by Django 4.0.3 on 2022-03-25 08:29

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0014_alter_product_sku_additional'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mart.colorsoption')),
            ],
        ),
        migrations.AddField(
            model_name='imagesoption',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mart.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.UUIDField(default=uuid.UUID('c2d09c24-8ac9-449c-8751-e797ff3cbc2a')),
        ),
        migrations.DeleteModel(
            name='Variants',
        ),
        migrations.AddField(
            model_name='variant',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mart.product'),
        ),
        migrations.AddField(
            model_name='variant',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mart.sizesoption'),
        ),
    ]
