# Generated by Django 3.1.1 on 2020-11-24 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_auto_20201007_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='choices',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='field',
            name='options',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='table',
            name='options',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
