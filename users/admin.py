from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db import models
from django.forms import CharField, Textarea, TextInput

from users.models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    search_fields = (
        "email",
        "name",
    )
    list_filter = ("email", "name", "is_active", "is_staff")
    ordering = ("-date_joined",)
    list_display = ("email", "name", "is_active", "is_staff")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "name",
                )
            },
        ),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )
    formfield_overrides = {
        models.TextField: {"widget": Textarea(attrs={"rows": 20, "cols": 60})},
    }
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "name", "password1", "password2", "is_active", "is_staff")}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
