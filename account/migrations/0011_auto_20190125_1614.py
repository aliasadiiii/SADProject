# Generated by Django 2.1.4 on 2019-01-25 16:14

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='phone',
            field=models.CharField(max_length=11, validators=[account.models.phone_validator]),
        ),
    ]