# Generated by Django 2.2 on 2019-05-15 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20190515_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='filef',
            field=models.FileField(default='', upload_to=''),
        ),
    ]