# Generated by Django 3.1.3 on 2020-11-22 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzasApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='value',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
