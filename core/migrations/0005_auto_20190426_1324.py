# Generated by Django 2.0.6 on 2019-04-26 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190425_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='city',
            field=models.CharField(max_length=16, null=True, verbose_name='市'),
        ),
        migrations.AddField(
            model_name='team',
            name='county',
            field=models.CharField(max_length=16, null=True, verbose_name='县'),
        ),
    ]
