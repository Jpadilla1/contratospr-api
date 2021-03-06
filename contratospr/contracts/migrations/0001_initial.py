# Generated by Django 2.1.3 on 2018-11-18 15:07

import contratospr.contracts.models
import contratospr.utils.fields
import django.contrib.postgres.fields.jsonb
import django.contrib.postgres.indexes
import django.contrib.postgres.search
import django.db.models.deletion
import django.utils.timezone
import django_extensions.db.fields
import django_s3_storage.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contract",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    contratospr.utils.fields.DateTimeCreatedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    "modified_at",
                    contratospr.utils.fields.DateTimeModifiedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                ("source_id", models.PositiveIntegerField(unique=True)),
                ("number", models.CharField(max_length=255)),
                ("amendment", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "slug",
                    django_extensions.db.fields.AutoSlugField(
                        blank=True,
                        editable=False,
                        populate_from=["number", "amendment", "source_id"],
                    ),
                ),
                ("date_of_grant", models.DateTimeField()),
                ("effective_date_from", models.DateTimeField()),
                ("effective_date_to", models.DateTimeField()),
                ("cancellation_date", models.DateTimeField(blank=True, null=True)),
                ("amount_to_pay", models.DecimalField(decimal_places=2, max_digits=20)),
                ("has_amendments", models.BooleanField()),
                ("exempt_id", models.CharField(max_length=255)),
                (
                    "search_vector",
                    django.contrib.postgres.search.SearchVectorField(null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Contractor",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    contratospr.utils.fields.DateTimeCreatedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    "modified_at",
                    contratospr.utils.fields.DateTimeModifiedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("source_id", models.PositiveIntegerField(unique=True)),
                ("entity_id", models.PositiveIntegerField(blank=True, null=True)),
                (
                    "slug",
                    django_extensions.db.fields.AutoSlugField(
                        blank=True, editable=False, populate_from=["name", "source_id"]
                    ),
                ),
            ],
            options={
                "ordering": ("-modified_at", "-created_at"),
                "get_latest_by": "modified_at",
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Document",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    contratospr.utils.fields.DateTimeCreatedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    "modified_at",
                    contratospr.utils.fields.DateTimeModifiedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                ("source_id", models.PositiveIntegerField(unique=True)),
                ("source_url", models.URLField()),
                (
                    "file",
                    models.FileField(
                        blank=True,
                        null=True,
                        storage=django_s3_storage.storage.S3Storage(),
                        upload_to=contratospr.contracts.models.document_file_path,
                    ),
                ),
                (
                    "pages",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        blank=True, null=True
                    ),
                ),
                (
                    "preview_data_file",
                    models.FileField(
                        blank=True,
                        null=True,
                        storage=django_s3_storage.storage.S3Storage(),
                        upload_to=contratospr.contracts.models.document_file_path,
                    ),
                ),
                (
                    "vision_data_file",
                    models.FileField(
                        blank=True,
                        null=True,
                        storage=django_s3_storage.storage.S3Storage(),
                        upload_to=contratospr.contracts.models.document_file_path,
                    ),
                ),
            ],
            options={
                "ordering": ("-modified_at", "-created_at"),
                "get_latest_by": "modified_at",
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Entity",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    contratospr.utils.fields.DateTimeCreatedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    "modified_at",
                    contratospr.utils.fields.DateTimeModifiedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("source_id", models.PositiveIntegerField(unique=True)),
                (
                    "slug",
                    django_extensions.db.fields.AutoSlugField(
                        blank=True, editable=False, populate_from="name"
                    ),
                ),
            ],
            options={"verbose_name_plural": "Entities"},
        ),
        migrations.CreateModel(
            name="Service",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    contratospr.utils.fields.DateTimeCreatedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    "modified_at",
                    contratospr.utils.fields.DateTimeModifiedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "slug",
                    django_extensions.db.fields.AutoSlugField(
                        blank=True, editable=False, populate_from="name"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ServiceGroup",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    contratospr.utils.fields.DateTimeCreatedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    "modified_at",
                    contratospr.utils.fields.DateTimeModifiedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "slug",
                    django_extensions.db.fields.AutoSlugField(
                        blank=True, editable=False, populate_from="name"
                    ),
                ),
            ],
            options={
                "ordering": ("-modified_at", "-created_at"),
                "get_latest_by": "modified_at",
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="service",
            name="group",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="contracts.ServiceGroup",
            ),
        ),
        migrations.AddField(
            model_name="contract",
            name="contractors",
            field=models.ManyToManyField(to="contracts.Contractor"),
        ),
        migrations.AddField(
            model_name="contract",
            name="document",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="contracts.Document",
            ),
        ),
        migrations.AddField(
            model_name="contract",
            name="entity",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="contracts.Entity",
            ),
        ),
        migrations.AddField(
            model_name="contract",
            name="parent",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="contracts.Contract",
            ),
        ),
        migrations.AddField(
            model_name="contract",
            name="service",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="contracts.Service",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="service", unique_together={("name", "group")}
        ),
        migrations.AddIndex(
            model_name="contract",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["search_vector"], name="contracts_c_search__513187_gin"
            ),
        ),
    ]
