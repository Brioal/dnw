# Generated by Django 2.0.6 on 2018-08-03 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_auto_20180803_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='doctor',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='接待医生'),
        ),
    ]
