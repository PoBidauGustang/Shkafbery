from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin

from .models import (
    AdditionalElements,
    BodyColour,
    BodyComplectation,
    CategoryAdditionalElements,
    CategoryBodyComplectation,
    ClosetType,
    Dimensions,
    Doorhandle,
    DoorsColours,
    DoorsMaterials,
    DoorsProfiles,
    DoorsSystem,
    FillingScheme,
)


class ClosetTypeAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = ClosetType
        fields = "__all__"


@admin.register(ClosetType)
class ClosetTypeAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "type",
        "description",
        "is_active",
    ]
    form = ClosetTypeAdminForm
    save_on_top = True
    save_as = True


class FillingSchemeAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = FillingScheme
        fields = "__all__"


class ClosetTypeInline(admin.TabularInline):
    model = ClosetType


@admin.register(FillingScheme)
class StepSpecificationValueAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "type",
        "description",
        "is_active",
    ]
    form = FillingSchemeAdminForm
    save_on_top = True
    save_as = True


# class StepSpecificationValueInline(admin.TabularInline):
#     model = StepSpecificationValue


# @admin.register(FillingScheme)
# class StepsAdmin(admin.ModelAdmin):
#     list_display = [
#         "id",
#         "name",
#     ]
#     inlines = [
#         StepSpecificationInline,
#         StepSpecificationValueInline,
#     ]


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = [
#         "title",
#         "description",
#         "slug",
#         "regular_price",
#         "discount_price",
#         "is_active",
#         "created_at",
#         "updated_at",
#     ]
#     filter_horizontal = ("category",)
#     list_filter = ["is_active", "created_at", "updated_at"]
#     list_editable = ["regular_price", "discount_price", "is_active"]
#     form = ProductAdminForm
#     inlines = [
#         ProductSpecificationValueInline,
#         ProductImageInline,
#     ]
#     prepopulated_fields = {"slug": ("title",)}
#     save_on_top = True
#     save_as = True
