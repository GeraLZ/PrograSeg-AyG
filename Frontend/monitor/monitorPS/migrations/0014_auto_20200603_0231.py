# Generated by Django 3.0.6 on 2020-06-03 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitorPS', '0013_auto_20200514_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default=None, max_length=110),
        ),
        migrations.AlterField(
            model_name='user',
            name='salt',
            field=models.CharField(default=None, max_length=25),
        ),
    ]
