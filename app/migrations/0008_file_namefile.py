# Generated by Django 2.2 on 2019-05-15 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20190515_0057'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='nameFile',
            field=models.CharField(default='', max_length=42),
        ),
    ]
