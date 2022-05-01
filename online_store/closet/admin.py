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
    list_display_links = ("type",)
    form = ClosetTypeAdminForm
    save_on_top = True
    save_as = True


class FillingSchemeAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = FillingScheme
        fields = "__all__"


class DimensionsInline(admin.TabularInline):
    model = Dimensions
    extra = 1


class BodyColourInline(admin.TabularInline):
    model = BodyColour.filling_scheme.through
    extra = 2


@admin.register(FillingScheme)
class FillingSchemeAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "type",
        "description",
        "is_active",
    ]
    list_display_links = ("name",)
    list_editable = ("type",)
    form = FillingSchemeAdminForm
    inlines = [
        DimensionsInline,
        BodyColourInline,
    ]
    save_on_top = True
    save_as = True


@admin.register(BodyColour)
class BodyColourAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "image",
        "alt_text",
    ]
    filter_horizontal = ("filling_scheme",)
    list_display_links = ("name",)
    save_on_top = True
    save_as = True


@admin.register(CategoryBodyComplectation)
class CategoryBodyComplectationAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "is_active",
    ]


class BodyComplectationForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = BodyComplectation
        fields = "__all__"


@admin.register(BodyComplectation)
class BodyComplectationAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "description",
        "image",
        "alt_text",
    ]
    form = BodyComplectationForm
    filter_horizontal = ("category", "filling_scheme")
    list_display_links = ("name",)
    save_on_top = True
    save_as = True


@admin.register(CategoryAdditionalElements)
class CategoryAdditionalElementsAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "is_active",
    ]


class AdditionalElementsForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = AdditionalElements
        fields = "__all__"


@admin.register(AdditionalElements)
class AdditionalElementsAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "description",
        "image",
        "alt_text",
    ]
    form = AdditionalElementsForm
    filter_horizontal = ("category", "filling_scheme")
    list_display_links = ("name",)
    save_on_top = True
    save_as = True


class DoorsSystemForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = DoorsSystem
        fields = "__all__"


class DoorsMaterialsInline(admin.TabularInline):
    model = DoorsMaterials.doors_system.through
    extra = 1


class DoorsProfilesInline(admin.TabularInline):
    model = DoorsProfiles.doors_system.through
    extra = 1


class DoorhandleInline(admin.TabularInline):
    model = Doorhandle.doors_system.through
    extra = 1


@admin.register(DoorsSystem)
class DoorsSystemAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "description",
        "is_active",
    ]
    form = DoorsSystemForm
    filter_horizontal = ("filling_scheme",)
    list_display_links = ("name",)
    inlines = [
        DoorsMaterialsInline,
        DoorsProfilesInline,
        DoorhandleInline,
    ]
    save_on_top = True
    save_as = True


class DoorsProfilesForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = DoorsProfiles
        fields = "__all__"


@admin.register(DoorsProfiles)
class DoorsProfilesAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "description",
        "image",
        "alt_text",
        "is_feature",
        "created_at",
        "updated_at",
    ]
    form = DoorsProfilesForm
    filter_horizontal = ("doors_system",)
    list_display_links = ("name",)
    save_on_top = True
    save_as = True


class DoorhandleForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Doorhandle
        fields = "__all__"


@admin.register(Doorhandle)
class DoorhandleAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "description",
        "image",
        "alt_text",
        "is_feature",
        "created_at",
        "updated_at",
    ]
    form = DoorhandleForm
    filter_horizontal = ("doors_system",)
    list_display_links = ("name",)
    save_on_top = True
    save_as = True


class DoorsMaterialsForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = DoorsMaterials
        fields = "__all__"


@admin.register(DoorsMaterials)
class DoorsMaterialsAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "description",
        "image",
        "alt_text",
        "is_feature",
        "created_at",
        "updated_at",
    ]
    form = DoorsMaterialsForm
    filter_horizontal = ("doors_system",)
    list_display_links = ("name",)
    save_on_top = True
    save_as = True
