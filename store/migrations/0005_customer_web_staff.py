# Generated by Django 2.0.6 on 2018-07-21 05:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0004_auto_20180721_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='web_staff',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='web_staff', to=settings.AUTH_USER_MODEL, verbose_name='网络客服'),
        ),
    ]
