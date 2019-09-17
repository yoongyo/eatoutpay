# Generated by Django 2.1 on 2019-09-17 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0009_auto_20190910_1547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='location_map',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='method',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='latitude',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='longitude',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
