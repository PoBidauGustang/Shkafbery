from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Category, Post


class PostAdminForm(forms.ModelForm):
    body = forms.CharField(label="Тело статьи", widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = "__all__"


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    list_display = [
        "name",
        "parent",
        "is_active",
    ]
    list_editable = ["parent", "is_active"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "publish", "status")
    form = PostAdminForm
    filter_horizontal = ("category",)
    list_filter = ("status", "created", "publish")
    search_fields = ("title", "body")
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "publish"
    ordering = ("status", "publish")
