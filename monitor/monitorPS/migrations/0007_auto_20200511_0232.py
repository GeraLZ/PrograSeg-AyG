# Generated by Django 3.0.6 on 2020-05-11 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitorPS', '0006_auto_20200511_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='codigo_token',
            field=models.CharField(blank=True, default=None, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='admin',
            name='salt',
            field=models.CharField(default='oOu6TuVIay7tiPENYFvD0A==', max_length=25),
        ),
    ]
