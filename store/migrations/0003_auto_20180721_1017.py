# Generated by Django 2.0.6 on 2018-07-21 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20180721_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='age',
            field=models.CharField(default='', max_length=20, null=True, verbose_name='年龄'),
        ),
    ]