# Generated by Django 2.1 on 2019-10-17 08:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0021_auto_20191017_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='admin',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
