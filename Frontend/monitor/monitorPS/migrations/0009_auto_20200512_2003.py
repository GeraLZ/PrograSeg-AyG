# Generated by Django 3.0.5 on 2020-05-12 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitorPS', '0008_auto_20200511_0242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='salt',
            field=models.CharField(default='vuDgq6QfmckcGT1viwEvTg==', max_length=25),
        ),
    ]