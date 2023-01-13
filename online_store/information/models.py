from django.db import models


class AboutCompany(models.Model):
    """
    The description of company.
    """

    title = models.CharField(
        verbose_name="заголовок",
        help_text="Обязательное",
        max_length=255,
        unique=False,
    )
    text = models.TextField(verbose_name="текст", blank=False)
    image = models.ImageField(
        verbose_name="изображение",
        help_text="Загрузите изображение компании",
        upload_to="main_page/about_company/%Y/%m/%d",
        default="planner/default.jpg",
        blank=True,
    )
    alt_text = models.CharField(
        verbose_name="альтернативный текст",
        help_text="Пожалуйста, добавьте альтернативный текст",
        max_length=255,
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(
        verbose_name="активно?",
        default=False,
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "О компании"
        verbose_name_plural = "О компании"

    def __str__(self):
        return self.title


class Examples(models.Model):
    """
    examples of our company work.
    """

    name = models.CharField(
        verbose_name="название примера",
        help_text="Обязательное и уникальное поле",
        max_length=255,
        unique=True,
    )
    description = models.TextField(
        verbose_name="описание", help_text="Not Required", blank=True
    )
    category = models.CharField(
        verbose_name="категория работ",
        default="",
        help_text="Обязательное и уникальное поле",
        max_length=255,
        blank=False,
    )
    price = models.DecimalField(
        verbose_name="цена",
        help_text="Maximum 9 999 999.99",
        error_messages={
            "name": {
                "max_length": "Цена должна быть в диапазоне от 0 до 9 999 999.99.",
            },
        },
        max_digits=9,
        decimal_places=0,
        null=True,
        blank=True,
    )
    for_main = models.BooleanField(
        verbose_name="для главной?",
        default=False,
    )
    is_active = models.BooleanField(
        verbose_name="активно?",
        default=True,
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "пример работы"
        verbose_name_plural = "примеры работ"

    def __str__(self):
        return self.name


class ExamplesPhoto(models.Model):
    """
    Examples photos.
    """

    examples = models.ManyToManyField(
        Examples,
        verbose_name="пример",
        related_name="filling_scheme_image",
        blank=True,
    )
    name = models.CharField(
        verbose_name="наименование",
        help_text="Обязательное и уникальное поле",
        max_length=255,
        unique=True,
    )
    image = models.ImageField(
        verbose_name="изображение",
        help_text="Загрузите изображение товара",
        upload_to="work_examples/%Y/%m/%d",
        default="planner/default.jpg",
        blank=True,
    )
    alt_text = models.CharField(
        verbose_name="Альтернативный текст",
        help_text="Пожалуйста, добавьте альтернативный текст",
        max_length=255,
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(
        verbose_name="активно?",
        default=True,
    )

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фото"

    def __str__(self):
        return self.name


class Faq(models.Model):
    """
    The FAQ.
    """

    name = models.CharField(
        verbose_name="название вопроса",
        help_text="Обязательное",
        max_length=255,
        unique=False,
    )
    question = models.TextField(verbose_name="вопрос", blank=False)
    answer = models.TextField(verbose_name="ответ", blank=False)
    is_active = models.BooleanField(
        verbose_name="активно?",
        default=True,
    )
    for_main = models.BooleanField(
        verbose_name="для главной?",
        default=False,
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQ"

    def __str__(self):
        return self.name


class MainPageHeader(models.Model):
    """
    The headers for main page.
    """

    title = models.CharField(
        verbose_name="заголовок",
        help_text="Обязательное",
        max_length=255,
        unique=False,
    )
    text = models.TextField(verbose_name="текст", blank=True)
    is_active = models.BooleanField(
        verbose_name="активно?",
        default=False,
        help_text="Допустима одна шапка в значении 'ДА', остальные - неизвестно",
        blank=True,
        null=True,
        unique=True,
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Шапка главной"
        verbose_name_plural = "Шапки главной"

    def __str__(self):
        return self.title


class Planner(models.Model):
    """
    The palnner info for main page.
    """

    title = models.CharField(
        verbose_name="заголовок",
        help_text="Обязательное",
        max_length=255,
        unique=False,
    )
    text = models.TextField(verbose_name="текст", blank=True)
    is_active = models.BooleanField(
        verbose_name="активно?",
        default=None,
        help_text="Допустима одна шапка в значении 'ДА', остальные - неизвестно",
        blank=True,
        null=True,
        unique=True,
    )
    image = models.ImageField(
        verbose_name="изображение",
        help_text="Загрузите изображение планировщика",
        upload_to="planner/main_page/%Y/%m/%d",
        default="planner/default.jpg",
        blank=True,
    )
    alt_text = models.CharField(
        verbose_name="Альтернативный текст",
        help_text="Пожалуйста, добавьте альтернативный текст",
        max_length=255,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Планировщик на главной"
        verbose_name_plural = "Планировщик на главной"

    def __str__(self):
        return self.title


class Services(models.Model):
    """
    Services of our company work.
    """

    name = models.CharField(
        verbose_name="название услуги",
        help_text="Обязательное и уникальное поле",
        max_length=255,
        unique=True,
    )
    short_description = models.TextField(
        verbose_name="краткое описание", help_text="Not Required", blank=True
    )
    description = models.TextField(
        verbose_name="описание", help_text="Not Required", blank=True
    )
    slug = models.SlugField(
        verbose_name="Category safe URL", max_length=255, unique=True
    )
    is_active = models.BooleanField(
        verbose_name="активно?",
        default=True,
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "услуга"
        verbose_name_plural = "услуги"

    def __str__(self):
        return self.name


class ServicesPhoto(models.Model):
    """
    Services photos.
    """

    services = models.ManyToManyField(
        Services,
        verbose_name="услуга",
        related_name="service_image",
        blank=True,
    )
    name = models.CharField(
        verbose_name="наименование",
        help_text="Обязательное и уникальное поле",
        max_length=255,
        unique=True,
    )
    image = models.ImageField(
        verbose_name="изображение",
        help_text="Загрузите изображение товара",
        upload_to="services/%Y/%m/%d",
        default="planner/default.jpg",
        blank=True,
    )
    alt_text = models.CharField(
        verbose_name="Альтернативный текст",
        help_text="Пожалуйста, добавьте альтернативный текст",
        max_length=255,
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(
        verbose_name="активно?",
        default=True,
    )

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фото"

    def __str__(self):
        return self.name
