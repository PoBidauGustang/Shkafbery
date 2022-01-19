from django.conf import settings
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, verbose_name="пользователь", on_delete=models.CASCADE
    )
    photo = models.ImageField(
        verbose_name="Фото", upload_to="users/%Y/%m/%d/", blank=True
    )
    town = models.CharField(
        verbose_name="город",
        help_text="Not Required",
        max_length=255,
        blank=True,
        null=True,
    )
    street = models.CharField(
        verbose_name="улица",
        help_text="Not Required",
        max_length=255,
        blank=True,
        null=True,
    )
    house = models.PositiveSmallIntegerField(
        verbose_name="дом", help_text="Not Required", blank=True, null=True
    )
    building = models.PositiveSmallIntegerField(
        verbose_name="корпус", help_text="Not Required", blank=True, null=True
    )
    apartment = models.PositiveSmallIntegerField(
        verbose_name="квартира", help_text="Not Required", blank=True, null=True
    )

    def __str__(self):
        return f"Profile for user {self.user}"

    class Meta:
        ordering = ("-user",)
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
