# Generated by Django 2.0.6 on 2018-08-11 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20180806_2152'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='instrument',
            options={'verbose_name': '器械录入', 'verbose_name_plural': '器械录入'},
        ),
        migrations.RenameField(
            model_name='instrument',
            old_name='instrument_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='productitems',
            old_name='pName',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='productitems',
            old_name='pnumber',
            new_name='number',
        ),
        migrations.RenameField(
            model_name='productitems',
            old_name='pprice',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='instrument',
            name='instrument_steps',
        ),
        migrations.RemoveField(
            model_name='productitems',
            name='steps',
        ),
    ]