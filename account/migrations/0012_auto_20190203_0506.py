# Generated by Django 2.1.4 on 2019-02-03 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_auto_20190125_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.Account'),
        ),
    ]