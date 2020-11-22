# Generated by Django 3.1.3 on 2020-11-22 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line1', models.CharField(max_length=150)),
                ('line2', models.CharField(blank=True, max_length=150, null=True)),
                ('city', models.CharField(max_length=50)),
                ('state_province', models.CharField(max_length=50)),
                ('postal_code', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=25)),
            ],
        ),
    ]