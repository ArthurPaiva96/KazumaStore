# Generated by Django 2.2.6 on 2019-10-24 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
