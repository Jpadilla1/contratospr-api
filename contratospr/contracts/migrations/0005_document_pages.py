# Generated by Django 2.1.2 on 2018-11-01 13:32

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0004_auto_20181027_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='pages',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]