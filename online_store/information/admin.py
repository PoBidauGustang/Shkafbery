from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin

from .models import AboutCompany, Examples, ExamplesPhoto, Faq


class AboutCompanyAdminForm(forms.ModelForm):
    text = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = AboutCompany
        fields = "__all__"


@admin.register(AboutCompany)
class ClosetTypeAdmin(admin.ModelAdmin):
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


class ExamplesAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Examples
        fields = "__all__"


class ExamplesPhotoInline(admin.TabularInline):
    model = ExamplesPhoto.examples.through
    extra = 1


@admin.register(Examples)
class ExamplesAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "description",
        "for_main",
        "is_active",
    ]
    list_display_links = ("name",)
    list_editable = ("is_active", "for_main")
    form = ExamplesAdminForm
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


class FaqAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Faq
        fields = "__all__"


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
