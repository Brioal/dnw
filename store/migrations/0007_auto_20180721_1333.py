# Generated by Django 2.0.6 on 2018-07-21 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_customer_store'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='store',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='web_staff', to='organization.LastStore', verbose_name='门店'),
        ),
    ]