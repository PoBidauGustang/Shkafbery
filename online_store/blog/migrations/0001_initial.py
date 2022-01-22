# Generated by Django 4.0.1 on 2022-01-22 18:35

import django.db.models.deletion
import django.utils.timezone
import mptt.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                        help_text="Required and unique",
                        max_length=255,
                        unique=True,
                        verbose_name="название категории",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        max_length=255,
                        unique=True,
                        verbose_name="безопасный URL категории",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="активна?"),
                ),
                ("lft", models.PositiveIntegerField(editable=False)),
                ("rght", models.PositiveIntegerField(editable=False)),
                ("tree_id", models.PositiveIntegerField(db_index=True, editable=False)),
                ("level", models.PositiveIntegerField(editable=False)),
                (
                    "parent",
                    mptt.fields.TreeForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="children",
                        to="blog.category",
                        verbose_name="родитель",
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=250, verbose_name="Заголовок")),
                ("slug", models.SlugField(max_length=250, unique_for_date="publish")),
                ("body", models.TextField(verbose_name="текст статьи")),
                (
                    "publish",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="опубликована"
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="создана"),
                ),
                (
                    "updated",
                    models.DateTimeField(auto_now=True, verbose_name="обновлена"),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("draft", "Draft"), ("published", "Published")],
                        default="draft",
                        max_length=10,
                        verbose_name="статус",
                    ),
                ),
                (
                    "category",
                    models.ManyToManyField(
                        related_name="blog_category",
                        to="blog.Category",
                        verbose_name="категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "статья",
                "verbose_name_plural": "статьи",
                "ordering": ("-publish",),
            },
        ),
    ]
