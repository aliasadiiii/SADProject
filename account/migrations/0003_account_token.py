# Generated by Django 2.1.4 on 2019-01-03 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20181221_2228'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='token',
            field=models.CharField(default='salam', max_length=10),
            preserve_default=False,
        ),
    ]
