# Generated by Django 2.2 on 2019-05-15 00:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20190514_2336'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publication',
            old_name='ContentPubli',
            new_name='contentPubli',
        ),
    ]
