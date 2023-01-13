# Generated by Django 4.0.1 on 2023-01-13 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("information", "0014_examples_category_examples_price"),
    ]

    operations = [
        migrations.CreateModel(
            name="Services",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Обязательное и уникальное поле",
                        max_length=255,
                        unique=True,
                        verbose_name="название услуги",
                    ),
                ),
                (
                    "short_description",
                    models.TextField(
                        blank=True, help_text="Not Required", verbose_name="описание"
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, help_text="Not Required", verbose_name="описание"
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        max_length=255, unique=True, verbose_name="Category safe URL"
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="активно?"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "услуга",
                "verbose_name_plural": "услуги",
            },
        ),
        migrations.CreateModel(
            name="ServicesPhoto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Обязательное и уникальное поле",
                        max_length=255,
                        unique=True,
                        verbose_name="наименование",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        default="planner/default.jpg",
                        help_text="Загрузите изображение товара",
                        upload_to="services/%Y/%m/%d",
                        verbose_name="изображение",
                    ),
                ),
                (
                    "alt_text",
                    models.CharField(
                        blank=True,
                        help_text="Пожалуйста, добавьте альтернативный текст",
                        max_length=255,
                        null=True,
                        verbose_name="Альтернативный текст",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="активно?"),
                ),
                (
                    "services",
                    models.ManyToManyField(
                        blank=True,
                        related_name="service_image",
                        to="information.Services",
                        verbose_name="услуга",
                    ),
                ),
            ],
            options={
                "verbose_name": "Фото",
                "verbose_name_plural": "Фото",
            },
        ),
    ]
