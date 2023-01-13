from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin

from .models import (
    AboutCompany,
    Examples,
    ExamplesPhoto,
    MainPageHeader,
    Faq,
    Planner,
    Services,
    ServicesPhoto,
)


class AboutCompanyAdminForm(forms.ModelForm):
    text = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = AboutCompany
        fields = "__all__"


@admin.register(AboutCompany)
class AboutCompanyAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "text",
        "image",
        "created_at",
        "updated_at",
        "is_active",
    ]
    list_display_links = ("title",)
    list_editable = ("is_active",)
    form = AboutCompanyAdminForm
    save_on_top = True
    save_as = True


# class ExamplesAdminForm(forms.ModelForm):
#     description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

#     class Meta:
#         model = Examples
#         fields = "__all__"


class ExamplesPhotoInline(admin.TabularInline):
    model = ExamplesPhoto.examples.through
    extra = 1


@admin.register(Examples)
class ExamplesAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "description",
        "category",
        "price",
        "for_main",
        "is_active",
    ]
    list_display_links = ("name",)
    list_editable = ("is_active", "for_main", "category", "price")
    inlines = [
        ExamplesPhotoInline,
    ]
    save_on_top = True
    save_as = True


@admin.register(ExamplesPhoto)
class ExamplesPhotoAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "image",
        "alt_text",
        "is_active",
    ]
    filter_horizontal = ("examples",)
    list_display_links = ("name",)
    list_editable = ("is_active",)
    save_on_top = True
    save_as = True


# class FaqAdminForm(forms.ModelForm):
#     description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

#     class Meta:
#         model = Faq
#         fields = "__all__"


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "question",
        "answer",
        "is_active",
        "for_main",
    ]
    list_display_links = ("name",)
    list_editable = ("is_active", "for_main")
    save_on_top = True
    save_as = True


@admin.register(MainPageHeader)
class MainPageHeaderAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "text",
        "is_active",
    ]
    exclude = ["created_at", "updated_at"]
    list_display_links = ("title",)
    list_editable = ("is_active",)
    save_on_top = True
    save_as = True


@admin.register(Planner)
class PlannerAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "text",
        "is_active",
        "image",
    ]
    exclude = ["created_at", "updated_at"]
    list_display_links = ("title",)
    list_editable = ("is_active",)
    save_on_top = True
    save_as = True


class ServicesPhotoInline(admin.TabularInline):
    model = ServicesPhoto.services.through
    extra = 1


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "description",
        "short_description",
        "is_active",
    ]
    list_display_links = ("name",)
    list_editable = ("is_active",)
    inlines = [
        ServicesPhotoInline,
    ]
    prepopulated_fields = {"slug": ("name",)}
    save_on_top = True
    save_as = True


@admin.register(ServicesPhoto)
class ServicesPhotoAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "image",
        "alt_text",
        "is_active",
    ]
    filter_horizontal = ("services",)
    list_display_links = ("name",)
    list_editable = ("is_active",)
    save_on_top = True
    save_as = True
