# Generated by Django 2.0.6 on 2018-06-27 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180627_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='date_of_birth',
            field=models.CharField(max_length=255, verbose_name='姓名'),
        ),
    ]