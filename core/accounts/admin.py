from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("email", "is_superuser", "is_active", "is_verified")
    list_filter = ("email", "is_active", "is_superuser", "is_verified")
    search_fields = ("email",)
    ordering = ("email",)

    fieldsets = (
        ("Users", {"fields": ("email", "password")}),
        (
            "Permissions",
            {"fields": ("is_staff", "is_superuser", "is_active", "is_verified")},
        ),
    )

    add_fieldsets = (
        (
            "User",
            {
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_superuser",
                    "is_active",
                    "is_verified",
                )
            },
        ),
    )


admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)
