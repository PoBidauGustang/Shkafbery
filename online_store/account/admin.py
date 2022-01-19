from django.contrib import admin

from .models import Profile

# from django.conf import settings
# from django.contrib.auth import get_user_model


# class UserInline(admin.TabularInline):
#     model = get_user_model()


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "photo", "town", "street", "house", "building", "apartment"]
    list_select_related = ("user",)
