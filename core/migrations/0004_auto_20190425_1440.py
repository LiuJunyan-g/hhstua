# Generated by Django 2.0.6 on 2019-04-25 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190425_1334'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopTen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peo_count', models.IntegerField(verbose_name='人数')),
                ('department', models.CharField(max_length=64, verbose_name='专业')),
            ],
        ),
        migrations.AlterField(
            model_name='fiveyears',
            name='peo_count',
            field=models.IntegerField(verbose_name='人数'),
        ),
        migrations.AlterField(
            model_name='fiveyears',
            name='year',
            field=models.IntegerField(verbose_name='年份'),
        ),
    ]