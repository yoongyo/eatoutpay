# Generated by Django 2.1 on 2019-10-01 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0017_auto_20191001_1411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='region',
        ),
        migrations.DeleteModel(
            name='City',
        ),
    ]