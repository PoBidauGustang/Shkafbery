from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from mptt.admin import MPTTModel, MPTTModelAdmin, TreeRelatedFieldListFilter

from .models import (
    Category,
    Color,
    ColorImage,
    ColorPrice,
    Product,
    ProductImage,
    ProductSpecification,
    ProductSpecificationValue,
    Dimensions,
    DimensionsValue,
    CategoryImage,
    # DimensionsPrice,
)


# class ProductAdminForm(forms.ModelForm):
#     description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

#     class Meta:
#         model = Product
#         fields = "__all__"


# class CategoryAdminForm(forms.ModelForm):
#     description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

#     class Meta:
#         model = Category
#         fields = "__all__"


# class ProductSpecificationInline(admin.TabularInline):
#     model = ProductSpecification


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    get_image.short_description = "Изображение"


class CategoryImageInline(admin.TabularInline):
    model = CategoryImage
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    get_image.short_description = "Изображение"


class ColorImageInline(admin.TabularInline):
    model = ColorImage
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    get_image.short_description = "Изображение"


class ProductSpecificationValueInline(admin.TabularInline):
    model = ProductSpecificationValue


class ColorPriceInline(admin.TabularInline):
    model = ColorPrice
    list_display = [
        "product",
        "color",
        "price_percent",
    ]
    readonly_fields = ("product",)
    extra = 2


class DimensionsValueInline(admin.TabularInline):
    model = DimensionsValue
    extra = 1


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    list_display = [
        "name",
        "parent",
        "description",
        "image",
        "position",
        "for_main_menu",
        "for_side_menu",
        "is_active",
    ]
    # form = CategoryAdminForm
    list_editable = [
        "parent",
        "is_active",
        "for_main_menu",
        "for_side_menu",
        "position",
        "image",
    ]
    inlines = [CategoryImageInline]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(ProductSpecification)
class ProductSpecificationAdmin(admin.ModelAdmin):
    model = Category
    list_filter = (("category", TreeRelatedFieldListFilter),)
    filter_horizontal = ("category",)


@admin.register(ProductSpecificationValue)
class ProductSpecificationValueAdmin(admin.ModelAdmin):
    list_filter = ("specification",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "description",
        "slug",
        "regular_price",
        "discount_price",
        "is_active",
        "popular",
        "created_at",
        "updated_at",
    ]
    filter_horizontal = ("category",)
    list_filter = ["is_active", "created_at", "updated_at"]
    list_editable = ["regular_price", "discount_price", "is_active", "popular"]
    # form = ProductAdminForm
    inlines = [
        ProductSpecificationValueInline,
        ProductImageInline,
        ColorPriceInline,
        DimensionsValueInline,
    ]
    prepopulated_fields = {"slug": ("title",)}
    save_on_top = True
    save_as = True


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    model = Category
    list_filter = (("category", TreeRelatedFieldListFilter),)
    filter_horizontal = ("category",)
    list_display = [
        "name",
        "is_active",
    ]
    list_editable = ["is_active"]
    inlines = [
        ColorImageInline,
    ]


@admin.register(ColorPrice)
class ColorPriceAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "product",
        "color",
        "price_percent",
    ]
    list_editable = [
        "price_percent",
    ]
    list_filter = ("product",)
    # inlines = [
    #     ColorImageInline,
    # ]


@admin.register(Dimensions)
class DimensionsAdmin(admin.ModelAdmin):
    model = Category
    list_filter = (("category", TreeRelatedFieldListFilter),)
    filter_horizontal = ("category",)
