# Generated by Django 2.2.6 on 2019-10-25 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sobre', '0002_auto_20191024_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='estilo',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
