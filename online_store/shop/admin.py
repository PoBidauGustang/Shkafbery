from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from mptt.admin import MPTTModel, MPTTModelAdmin, TreeRelatedFieldListFilter

from .models import (
    Category,
    Product,
    ProductImage,
    ProductSpecification,
    ProductSpecificationValue,
)


class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Product
        fields = "__all__"


class CategoryAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Category
        fields = "__all__"


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    list_display = [
        "name",
        "parent",
        "description",
        "image",
        "position",
        "for_main",
        "is_active",
    ]
    form = CategoryAdminForm
    list_editable = ["parent", "is_active", "for_main", "position", "image"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(ProductSpecification)
class ProductSpecificationAdmin(admin.ModelAdmin):
    model = Category
    list_filter = (("category", TreeRelatedFieldListFilter),)
    filter_horizontal = ("category",)


class ProductSpecificationInline(admin.TabularInline):
    model = ProductSpecification


@admin.register(ProductSpecificationValue)
class ProductSpecificationValueAdmin(admin.ModelAdmin):
    list_filter = ("specification",)


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
        "title",
        "description",
        "slug",
        "regular_price",
        "discount_price",
        "is_active",
        "created_at",
        "updated_at",
    ]
    filter_horizontal = ("category",)
    list_filter = ["is_active", "created_at", "updated_at"]
    list_editable = ["regular_price", "discount_price", "is_active"]
    form = ProductAdminForm
    inlines = [
        ProductSpecificationValueInline,
        ProductImageInline,
    ]
    prepopulated_fields = {"slug": ("title",)}
    save_on_top = True
    save_as = True
