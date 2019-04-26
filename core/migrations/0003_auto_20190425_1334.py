# Generated by Django 2.0.6 on 2019-04-25 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190424_2031'),
    ]

    operations = [
        migrations.CreateModel(
            name='FiveYears',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peo_count', models.IntegerField(max_length='64', verbose_name='人数')),
                ('year', models.IntegerField(max_length=16, verbose_name='年份')),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='sex',
            field=models.CharField(max_length=4, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='sex',
            field=models.CharField(max_length=4, verbose_name='性别'),
        ),
    ]