from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey

# class Post(models.Model):
#     title = models.CharField("Посты", max_length=150)
#     text = models.TextField("Текст")
#     url = models.SlugField(max_length=160, unique=True)
#     class Meta:
#         verbose_name = "Пост"
#         verbose_name_plural = "Посты"

#     def __str__(self):
#         return self.name

#     # def get_absolute_url(self):
#     #     return reverse("_detail", kwargs={"pk": self.pk})


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ("name",)
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("shop:product_list_by_category", args=[self.slug])


class SubCategory(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    fk_category = models.ForeignKey(
        Category, related_name="subcategory", on_delete=models.SET_NULL, null=True
    )

    class Meta:
        ordering = ("name",)
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"

    def __str__(self):
        return self.name


class Value(models.Model):
    # name = models.ForeignKey(
    #     Attribute, related_name="value_attribute", on_delete=models.CASCADE
    # )
    name = models.CharField(max_length=200, db_index=True)
    # value = models.CharField(max_length=200, db_index=True, blank=True)

    class Meta:
        verbose_name = "Значение"
        verbose_name_plural = "Значения"

    def __str__(self):
        return self.name


class Attribute(models.Model):
    # name = models.CharField(max_length=200, db_index=True)
    name = models.ForeignKey(Value, verbose_name="Свойство", on_delete=models.CASCADE)
    # value =  models.ForeignKey(
    #     'Value', related_name="attribute_value", on_delete=models.CASCADE
    # )
    # value = models.IntegerField("Значение", default=0)
    value = models.CharField(max_length=200, db_index=True)

    class Meta:
        ordering = ("name",)
        verbose_name = "Свойство"
        verbose_name_plural = "Свойства"

    def __str__(self):
        return self.value


class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    category = models.ManyToManyField(
        SubCategory,
        verbose_name="подкатегория",
        related_name="products_subcategory",
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    attribute = models.ManyToManyField(
        Attribute,
        verbose_name="свойство",
        related_name="products_attribute",
    )
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("name",)
        # index_together = (("id", "slug"),)
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("shop:product_detail", args=[self.id, self.slug])


class Image(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    image = models.ImageField("Изображения", upload_to="products/%Y/%m/%d", blank=True)
    fk_product = models.ForeignKey(
        Product, related_name="image", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ("name",)
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def __str__(self):
        return self.name
