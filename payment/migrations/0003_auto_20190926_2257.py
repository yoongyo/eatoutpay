# Generated by Django 2.1 on 2019-09-26 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_auto_20190920_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='menus',
            field=models.TextField(),
        ),
    ]
