# Generated by Django 3.0.6 on 2020-05-11 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitorPS', '0004_auto_20200507_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='salt',
            field=models.CharField(default='i+mMAWDrFDgozg5Qnkedbg==', max_length=25),
        ),
    ]