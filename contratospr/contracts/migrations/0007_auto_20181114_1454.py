# Generated by Django 2.1.3 on 2018-11-14 14:54

import django.contrib.postgres.indexes
import django.contrib.postgres.search
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0006_auto_20181113_1641'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contract',
            options={},
        ),
        migrations.AddField(
            model_name='contract',
            name='search_vector',
            field=django.contrib.postgres.search.SearchVectorField(null=True),
        ),
        migrations.AddIndex(
            model_name='contract',
            index=django.contrib.postgres.indexes.GinIndex(fields=['search_vector'], name='contracts_c_search__513187_gin'),
        ),
    ]