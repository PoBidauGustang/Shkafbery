# Generated by Django 4.0.1 on 2023-01-13 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("information", "0002_alter_aboutcompany_options_alter_faq_options_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="MainPageHeader",
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
                    "title",
                    models.CharField(
                        help_text="Обязательное",
                        max_length=255,
                        verbose_name="заголовок",
                    ),
                ),
                ("text", models.TextField(blank=True, verbose_name="текст")),
                (
                    "is_active",
                    models.BooleanField(
                        default=False, unique=True, verbose_name="активно?"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Шапка главной",
                "verbose_name_plural": "Шапки главной",
            },
        ),
    ]
