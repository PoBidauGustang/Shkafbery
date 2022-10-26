from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField


class Category(MPTTModel):
    """
    Category Table implimented with MPTT.
    """

    name = models.CharField(
        verbose_name="Category Name",
        help_text="Required and unique",
        max_length=255,
        unique=True,
    )
    slug = models.SlugField(
        verbose_name="Category safe URL", max_length=255, unique=True
    )
    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )
    description = models.TextField(
        verbose_name="описание", help_text="Not Required", blank=True
    )
    for_main = models.BooleanField(
        verbose_name="для главной?",
        default=False,
    )
    image = models.ImageField(
        verbose_name="изображение",
        help_text="Загрузите изображение категории",
        upload_to="planner/shop/category/%Y/%m/%d",
        default="planner/default.jpg",
        blank=True,
    )
    position = models.IntegerField(
        verbose_name="Позиция в категории",
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(default=True)

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    # def get_absolute_url(self):
    #     return reverse("shop:category_list", args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    The Product table contining all product items.
    """

    title = models.CharField(
        verbose_name="Название",
        help_text="Required",
        max_length=255,
    )
    category = models.ManyToManyField(
        Category,
        verbose_name="категория",
        related_name="products_category",
    )
    description = models.TextField(
        verbose_name="описание", help_text="Not Required", blank=True
    )
    slug = models.SlugField(max_length=255)
    regular_price = models.DecimalField(
        verbose_name="обычная цена",
        help_text="Maximum 9 999 999.99",
        error_messages={
            "name": {
                "max_length": "Цена должна быть в диапазоне от 0 до 9 999 999.99.",
            },
        },
        max_digits=9,
        decimal_places=2,
        null=True,
        blank=True,
    )
    discount_price = models.DecimalField(
        verbose_name="Discount price",
        help_text="Maximum 9 999 999.99",
        error_messages={
            "name": {
                "max_length": "Цена должна быть в диапазоне от 0 до 9 999 999.99.",
            },
        },
        max_digits=9,
        decimal_places=2,
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(
        verbose_name="Видимость товара",
        help_text="Изменить видимость товара",
        default=True,
    )
    created_at = models.DateTimeField("Создан", auto_now_add=True, editable=False)
    updated_at = models.DateTimeField("Обновлен", auto_now=True)
    # users_wishlist = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="user_wishlist", blank=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    # def get_absolute_url(self):
    #     return reverse("shop:product_detail", args=[self.slug])

    def __str__(self):
        return self.title


class ProductSpecification(models.Model):
    """
    The Product Specification Table contains product
    specifiction or features for the product types.
    """

    name = models.CharField(
        verbose_name="Имя", help_text="Required", max_length=255, unique=True
    )
    category = models.ManyToManyField(
        Category,
        verbose_name="категория",
        related_name="products_specification_category",
    )

    class Meta:
        verbose_name = "Свойство товара"
        verbose_name_plural = "Свойства товаров"

    def __str__(self):
        return self.name


class ProductSpecificationValue(models.Model):
    """
    The Product Specification Value table holds each of the
    products individual specification or bespoke features.
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    specification = models.ForeignKey(
        ProductSpecification,
        verbose_name="Свойство",
        on_delete=models.RESTRICT,
    )
    value = models.CharField(
        verbose_name="значение",
        help_text="Значение свойства товара (maximum of 255 words)",
        max_length=255,
    )

    class Meta:
        verbose_name = "Значение свойства товара"
        verbose_name_plural = "Значения свойства товаров"

    def __str__(self):
        return self.value


class ProductImage(models.Model):
    """
    The Product Image table.
    """

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_image"
    )
    image = models.ImageField(
        verbose_name="Изображение",
        help_text="Загрузите изображение товара",
        upload_to="products/%Y/%m/%d",
        default="products/default.jpg",
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
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"


class CategoryImage(models.Model):
    """
    The Category Image table.
    """

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="category_image"
    )
    image = models.ImageField(
        verbose_name="Изображение",
        help_text="Загрузите изображение категории",
        upload_to="products_category/%Y/%m/%d",
        default="products/default.jpg",
        blank=True,
    )
    alt_text = models.CharField(
        verbose_name="Альтернативный текст",
        help_text="Пожалуйста, добавьте альтернативный текст",
        max_length=255,
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(default=True)
    for_main = models.BooleanField(
        verbose_name="для меню?",
        default=False,
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"


class Color(models.Model):
    """
    The Product colors
    """

    name = models.CharField(
        verbose_name="Название", help_text="Required", max_length=255, unique=True
    )
    category = models.ManyToManyField(
        Category,
        verbose_name="категория",
        related_name="products_color_category",
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Цвет товара"
        verbose_name_plural = "Цвета товаров"

    def __str__(self):
        return self.name


class ColorImage(models.Model):
    """
    The Product Color table.
    """

    color = models.ForeignKey(
        "ColorPrice", on_delete=models.CASCADE, related_name="color_image"
    )
    image = models.ImageField(
        verbose_name="Цвет",
        help_text="Загрузите фото цвета товара",
        upload_to="products/colors/%Y/%m/%d",
        default="products/colors/default.jpg",
        blank=True,
    )
    alt_text = models.CharField(
        verbose_name="Альтернативный текст",
        help_text="Пожалуйста, добавьте альтернативный текст",
        max_length=255,
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Фото цвета товара"
        verbose_name_plural = "Фото цветов товаров"


class ColorPrice(models.Model):
    """
    The price of product`s color in percent.
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(
        Color,
        verbose_name="Цвет",
        on_delete=models.RESTRICT,
    )
    price_percent = models.IntegerField(
        validators=[MinValueValidator(-100), MaxValueValidator(100)],
        verbose_name="Добавленная стоимость в %",
        help_text="Изменение цены товара за цвет в %",
        default=0,
    )

    class Meta:
        verbose_name = "Изменение цены товара за цвет"
        verbose_name_plural = "Изменение цен товаров за цвета"


class Dimensions(models.Model):
    """
    The Product dimensions
    """

    name = models.CharField(
        verbose_name="Название", help_text="Required", max_length=255, unique=True
    )
    category = models.ManyToManyField(
        Category,
        verbose_name="категория",
        related_name="products_dimensions_category",
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Размер товара"
        verbose_name_plural = "Размеры товаров"

    def __str__(self):
        return self.name


class DimensionsValue(models.Model):
    """
    The Product Dimensions Value table holds values with it`s price change of all dimesion types.
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    dimension = models.ForeignKey(
        Dimensions,
        verbose_name="Размеры",
        on_delete=models.RESTRICT,
    )
    value = models.CharField(
        verbose_name="Значение",
        help_text="Значение размера товара в мм, для п.м. указывается ширина 1 п.м, для ШГВ - ШхГхВ, для ДШ - ДхШ",
        max_length=255,
    )
    price_change = models.IntegerField(
        verbose_name="Изменение цены от размера",
        help_text="Изменение цены товара от размеров",
        default=0,
    )

    class Meta:
        verbose_name = "Значение размера и изменение цены"
        verbose_name_plural = "Значения размеров изменение цен"
