# Generated by Django 3.1.3 on 2020-11-22 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordersApp', '0005_auto_20201122_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='value',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7, null=True),
        ),
    ]
