# Generated by Django 2.2 on 2019-05-13 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='belong',
            name='idAccountB',
            field=models.ForeignKey(db_column='idAccountB', on_delete=django.db.models.deletion.CASCADE, to='app.Account'),
        ),
        migrations.AlterField(
            model_name='belong',
            name='idGroupB',
            field=models.ForeignKey(db_column='idGroupB', on_delete=django.db.models.deletion.CASCADE, to='app.Group'),
        ),
        migrations.AlterField(
            model_name='category',
            name='groupCat',
            field=models.ForeignKey(db_column='groupCat', null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Group'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='idAccountC',
            field=models.ForeignKey(db_column='idAccountC', on_delete=django.db.models.deletion.CASCADE, to='app.Account'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='idPubliC',
            field=models.ForeignKey(db_column='idPubliC', on_delete=django.db.models.deletion.CASCADE, to='app.Publication'),
        ),
        migrations.AlterField(
            model_name='group',
            name='idAccountGroup',
            field=models.ForeignKey(db_column='idAccountGroup', on_delete=django.db.models.deletion.CASCADE, to='app.Account'),
        ),
        migrations.AlterField(
            model_name='join',
            name='idAccountJ',
            field=models.ForeignKey(db_column='idAccountJ', on_delete=django.db.models.deletion.CASCADE, to='app.Account'),
        ),
        migrations.AlterField(
            model_name='join',
            name='idGroupJ',
            field=models.ForeignKey(db_column='idGroupJ', on_delete=django.db.models.deletion.CASCADE, to='app.Group'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='idAccountPubli',
            field=models.ForeignKey(db_column='idAccountPubli', on_delete=django.db.models.deletion.CASCADE, to='app.Account'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='idCatPubli',
            field=models.ForeignKey(db_column='idCatPubli', on_delete=django.db.models.deletion.CASCADE, to='app.Category'),
        ),
        migrations.DeleteModel(
            name='File',
        ),
    ]
