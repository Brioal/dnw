# Generated by Django 2.0.6 on 2018-06-18 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vin_search', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vin_product',
            options={'verbose_name': 'VIN产品', 'verbose_name_plural': 'VIN产品列表'},
        ),
        migrations.AlterField(
            model_name='product_cartype',
            name='product_code',
            field=models.CharField(max_length=128),
        ),
    ]