# Generated by Django 3.0.7 on 2023-10-19 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_auto_20231019_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='doors',
            field=models.CharField(choices=[('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=10),
        ),
    ]
