# Generated by Django 2.1.4 on 2019-01-07 00:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20190106_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='join_date',
            field=models.DateTimeField(auto_created=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
