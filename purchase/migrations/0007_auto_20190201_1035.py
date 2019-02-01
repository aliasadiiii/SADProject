# Generated by Django 2.1.4 on 2019-02-01 10:35

from django.db import migrations, models
import purchase.models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0006_auto_20190201_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='reference_token',
            field=models.CharField(default=purchase.models.generate_random_token, max_length=10, unique=True),
        ),
    ]
