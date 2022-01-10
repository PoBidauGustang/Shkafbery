from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from mptt.admin import MPTTModelAdmin

from .models import (
    Category,
    Product,
    ProductImage,  # ProductType,
    ProductSpecification,
    ProductSpecificationValue,
)

admin.site.register(Category, MPTTModelAdmin)


class ProductSpecificationInline(admin.TabularInline):
    model = ProductSpecification


# @admin.register(ProductType)
# class ProductTypeAdmin(admin.ModelAdmin):
#     inlines = [
#         ProductSpecificationInline,
#     ]


@admin.register(ProductSpecification)
class ProductSpecificationAdmin(admin.ModelAdmin):
    ...


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    get_image.short_description = "Изображение"


class ProductSpecificationValueInline(admin.TabularInline):
    model = ProductSpecificationValue


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        # "product_type",
        "title",
        # "category",
        "description",
        "slug",
        "regular_price",
        "discount_price",
        "is_active",
        "created_at",
        "updated_at",
    ]
    list_filter = ["is_active", "created_at", "updated_at"]
    list_editable = ["regular_price", "discount_price", "is_active"]
    inlines = [
        ProductSpecificationValueInline,
        ProductImageInline,
    ]
    prepopulated_fields = {"slug": ("title",)}
