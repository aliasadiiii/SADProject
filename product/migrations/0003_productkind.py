# Generated by Django 2.1.4 on 2019-01-03 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20181221_1016'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductKind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=50)),
            ],
        ),
    ]