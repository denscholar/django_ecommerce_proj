from django.contrib import admin
from accounts.models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "email",
        "username",
        "phone_number",
        "date_joined",
        "last_login",
        "is_active",
    )
    search_field = ("email", "phone_number")
    readonly_fields = ("id", "date_joined", "last_login")


admin.site.register(CustomUser, CustomUserAdmin)
