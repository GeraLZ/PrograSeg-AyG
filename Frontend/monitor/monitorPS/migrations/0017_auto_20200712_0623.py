# Generated by Django 3.0.6 on 2020-07-12 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitorPS', '0016_auto_20200712_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servers',
            name='api_iv',
            field=models.CharField(blank=True, default=None, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='servers',
            name='api_password',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
