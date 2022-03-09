from django.db import models


class ClosetType(models.Model):
    """
    Category Type of Closet.
    """

    type = models.CharField(
        verbose_name="количество дверей",
        help_text="Обязательное и уникальное поле",
        max_length=255,
        unique=True,
    )
    description = models.TextField(
        verbose_name="описание", help_text="Not Required", blank=True
    )
    is_active = models.BooleanField(verbose_name="активный?", default=True)

    class Meta:
        verbose_name = "Тип шкафа"
        verbose_name_plural = "Типы шкафов"

    def __str__(self):
        return self.type


class FillingScheme(models.Model):
    """
    Filling Scheme Table.
    """

    name = models.CharField(
        verbose_name="название",
        help_text="Обязательное и уникальное поле",
        max_length=255,
        unique=True,
    )
    type = models.ForeignKey(
        ClosetType,
        on_delete=models.CASCADE,
        verbose_name="тип",
        related_name="type_filling_scheme",
    )
    description = models.TextField(
        verbose_name="описание", help_text="Not Required", blank=True
    )
    is_active = models.BooleanField(verbose_name="активная?", default=True)

    class Meta:
        verbose_name = "Схема наполнения"
        verbose_name_plural = "Схемы наполнения"

    def __str__(self):
        return self.name


class Dimensions(models.Model):
    """
    Closet Dimensions Table.
    """

    filling_scheme = models.ForeignKey(
        FillingScheme,
        on_delete=models.CASCADE,
        related_name="filling_scheme_dimensions",
    )
    min_width = models.IntegerField(
        verbose_name="Минимальная ширина",
        null=False,
        blank=False,
    )
    max_width = models.IntegerField(
        verbose_name="Максимальная ширина",
        null=False,
        blank=False,
    )
    min_height = models.IntegerField(
        verbose_name="Минимальная высота",
        null=False,
        blank=False,
    )
    max_height = models.IntegerField(
        verbose_name="Максимальная высота",
        null=False,
        blank=False,
    )
    min_depth = models.IntegerField(
        verbose_name="Минимальная глубина",
        null=False,
        blank=False,
    )
    max_depth = models.IntegerField(
        verbose_name="Максимальная глубина",
        null=False,
        blank=False,
    )

    class Meta:
        verbose_name = "Размер шкафа"
        verbose_name_plural = "Размеры шкафов"


class BodyColour(models.Model):
    """
    Body Coloure Table.
    """

    filling_scheme = models.ManyToManyField(
        FillingScheme,
        verbose_name="схема наполнения",
        related_name="filling_scheme_image",
    )
    name = models.CharField(
        verbose_name="наименование",
        help_text="Обязательное и уникальное поле",
        max_length=255,
        unique=True,
    )
    image = models.ImageField(
        verbose_name="Фото цвета",
        help_text="Загрузите изображение",
        upload_to="configurator/body/%Y/%m/%d",
        default="configurator/default.jpg",
        blank=True,
    )
    alt_text = models.CharField(
        verbose_name="Альтернативный текст",
        help_text="Пожалуйста, добавьте альтернативный текст",
        max_length=255,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Цвет корпуса"
        verbose_name_plural = "Цвета корпуса"

    def __str__(self):
        return self.name


class CategoryBodyComplectation(models.Model):
    """
    Category of Body Complectation Table.
    """

    name = models.CharField(
        verbose_name="категория",
        help_text="Обязательное и уникальное поле",
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(verbose_name="активная?", default=True)

    class Meta:
        verbose_name = "категория комплектации корпуса"
        verbose_name_plural = "категории комплектации корпусов"

    def __str__(self):
        return self.name


class BodyComplectation(models.Model):
    """
    Body Complectation Table.
    """

    name = models.CharField(
        verbose_name="название",
        help_text="Обязательное и уникальное поле",
        max_length=255,
        unique=True,
    )
    filling_scheme = models.ManyToManyField(
        FillingScheme,
        verbose_name="схема наполнения",
        related_name="filling_scheme_body_complectation",
    )
    category = models.ManyToManyField(
        CategoryBodyComplectation,
        verbose_name="категория",
        related_name="category_body_complectation",
    )
    description = models.TextField(
        verbose_name="описание", help_text="Not Required", blank=True
    )
    image = models.ImageField(
        verbose_name="Фото элемента'",
        help_text="Загрузите изображение",
        upload_to="planner/complectation/%Y/%m/%d",
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

    class Meta:
        verbose_name = "комплектация корпуса"
        verbose_name_plural = "комплектация корпуса"

    def __str__(self):
        return self.name


class CategoryAdditionalElements(models.Model):
    """
    Category of Additional Elements Table.
    """

    name = models.CharField(
        verbose_name="категория",
        help_text="Обязательное и уникальное поле",
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(verbose_name="активная?", default=True)

    class Meta:
        verbose_name = "категория дополнительных элементов"
        verbose_name_plural = "категории дополнительных элементов"

    def __str__(self):
        return self.name


class AdditionalElements(models.Model):
    """
    Additional Elements Table.
    """

    name = models.CharField(
        verbose_name="название",
        help_text="Обязательное и уникальное поле",
        max_length=255,
        unique=True,
    )
    filling_scheme = models.ManyToManyField(
        FillingScheme,
        verbose_name="схема наполнения",
        related_name="filling_scheme_additional_elements",
    )
    category = models.ManyToManyField(
        CategoryAdditionalElements,
        verbose_name="категория",
        related_name="category_additional_elements",
    )
    description = models.TextField(
        verbose_name="описание", help_text="Not Required", blank=True
    )
    image = models.ImageField(
        verbose_name="Фото элемента'",
        help_text="Загрузите изображение",
        upload_to="planner/additional_elements/%Y/%m/%d",
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

    class Meta:
        verbose_name = "дополнительный элемент"
        verbose_name_plural = "дополнительные элементы"

    def __str__(self):
        return self.name


class DoorsSystem(models.Model):
    """
    Doors System Table.
    """

    name = models.CharField(
        verbose_name="название",
        help_text="Обязательное и уникальное поле",
        max_length=255,
        unique=True,
    )
    filling_scheme = models.ManyToManyField(
        FillingScheme,
        verbose_name="схема наполнения",
        related_name="filling_scheme_doors_system",
    )
    description = models.TextField(
        verbose_name="описание", help_text="Not Required", blank=True
    )
    is_active = models.BooleanField(verbose_name="активная?", default=True)

    class Meta:
        verbose_name = "система дверей"
        verbose_name_plural = "системы дверей"

    def __str__(self):
        return self.name


class DoorsColours(models.Model):
    """
    The Doors Colours Image table.
    """

    name = models.CharField(
        verbose_name="название",
        help_text="Обязательное и уникальное поле",
        max_length=255,
        unique=True,
    )
    doors_system = models.ForeignKey(
        DoorsSystem, on_delete=models.CASCADE, related_name="doors_system_doors_colours"
    )
    image = models.ImageField(
        verbose_name="Изображение",
        help_text="Загрузите изображение товара",
        upload_to="planner/doors/colour/%Y/%m/%d",
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
    is_feature = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "цвет дверей"
        verbose_name_plural = "цвета дверей"

    def __str__(self):
        return self.name


class DoorsProfiles(models.Model):
    """
    The Doors Profiles table.
    """

    name = models.CharField(
        verbose_name="название",
        help_text="Обязательное и уникальное поле",
        max_length=255,
        unique=True,
    )
    doors_system = models.ForeignKey(
        DoorsSystem,
        on_delete=models.CASCADE,
        related_name="doors_system_doors_profiles",
    )
    image = models.ImageField(
        verbose_name="Изображение",
        help_text="Загрузите изображение товара",
        upload_to="planner/doors/profile/%Y/%m/%d",
        default="planner/default.jpg",
        blank=True,
    )
    description = models.TextField(
        verbose_name="описание", help_text="Not Required", blank=True
    )
    alt_text = models.CharField(
        verbose_name="Альтернативный текст",
        help_text="Пожалуйста, добавьте альтернативный текст",
        max_length=255,
        null=True,
        blank=True,
    )
    is_feature = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "дверной профиль"
        verbose_name_plural = "дверные профили"

    def __str__(self):
        return self.name


class Doorhandle(models.Model):
    """
    The Doorhandle table.
    """

    name = models.CharField(
        verbose_name="название",
        help_text="Обязательное и уникальное поле",
        max_length=255,
        unique=True,
    )
    doors_system = models.ForeignKey(
        DoorsSystem, on_delete=models.CASCADE, related_name="doors_system_doorhandle"
    )
    image = models.ImageField(
        verbose_name="Изображение",
        help_text="Загрузите изображение товара",
        upload_to="planner/doors/handle/%Y/%m/%d",
        default="planner/default.jpg",
        blank=True,
    )
    description = models.TextField(
        verbose_name="описание", help_text="Not Required", blank=True
    )
    alt_text = models.CharField(
        verbose_name="Альтернативный текст",
        help_text="Пожалуйста, добавьте альтернативный текст",
        max_length=255,
        null=True,
        blank=True,
    )
    is_feature = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "дверная ручка"
        verbose_name_plural = "дверные ручки"

    def __str__(self):
        return self.name


class DoorsMaterials(models.Model):
    """
    The Doors materials table.
    """

    name = models.CharField(
        verbose_name="название материала",
        help_text="Обязательное и уникальное поле",
        max_length=255,
        unique=True,
    )
    filling_scheme = models.ManyToManyField(
        FillingScheme,
        verbose_name="схема наполнения",
        related_name="filling_scheme_doors_materials",
    )
    image = models.ImageField(
        verbose_name="Изображение",
        help_text="Загрузите изображение товара",
        upload_to="planner/doors/materials/%Y/%m/%d",
        default="planner/default.jpg",
        blank=True,
    )
    description = models.TextField(
        verbose_name="описание", help_text="Not Required", blank=True
    )
    alt_text = models.CharField(
        verbose_name="Альтернативный текст",
        help_text="Пожалуйста, добавьте альтернативный текст",
        max_length=255,
        null=True,
        blank=True,
    )
    is_feature = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "материал дверей"
        verbose_name_plural = "материалы дверей"

    def __str__(self):
        return self.name
