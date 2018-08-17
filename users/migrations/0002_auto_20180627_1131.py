# Generated by Django 2.0.6 on 2018-06-27 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.CharField(max_length=255, unique=True, verbose_name='手机号'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='is_admin',
            field=models.BooleanField(default=True),
        ),
    ]