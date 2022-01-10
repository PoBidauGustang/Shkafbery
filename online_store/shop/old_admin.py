from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Attribute, Category, Image, Product, SubCategory, Value


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    get_image.short_description = "Изображение"


# class AttributeInline(admin.TabularInline):
#     model = Attribute
#     extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "slug",
        "price",
        "description",
        "created",
        "updated",
        "available",
    ]
    list_filter = ["available", "created", "updated"]
    list_editable = ["price", "available"]
    inlines = [ImageInline]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "image", "get_image", "fk_product"]
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        # return mark_safe(f'<img src={obj.image.url} width="50" height="60"')
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    get_image.short_description = "Изображение"


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "fk_category"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ["name", "value"]


@admin.register(Value)
class ValueAdmin(admin.ModelAdmin):
    list_display = ["name"]
