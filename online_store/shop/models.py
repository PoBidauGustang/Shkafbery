from django.conf import settings
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
        verbose_name = "Спецификация товара"
        verbose_name_plural = "Спецификации товаров"

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
        # null=True,
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


class ProductSpecificationValue(models.Model):
    """
    The Product Specification Value table holds each of the
    products individual specification or bespoke features.
    """

    # def get_total_cost(self):
    #     results = self.Product.objects.all()
    #     end = []
    #     for result in results:
    #         end += result.category.all()
    #     return end

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    specification = models.ForeignKey(
        ProductSpecification,
        verbose_name="Свойство",
        on_delete=models.RESTRICT,
        # limit_choices_to={'category': get_total_cost(product)},
    )
    value = models.CharField(
        verbose_name="значение",
        help_text="Значение характеристики товара (maximum of 255 words)",
        max_length=255,
    )

    class Meta:
        verbose_name = "Значение характеристики товара"
        verbose_name_plural = "Значения характеристик товаров"

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
