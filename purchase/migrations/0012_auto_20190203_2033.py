# Generated by Django 2.0.10 on 2019-02-03 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0011_purchase_geolocation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='geolocation',
        ),
        migrations.AddField(
            model_name='purchase',
            name='locationX',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='purchase',
            name='locationY',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]