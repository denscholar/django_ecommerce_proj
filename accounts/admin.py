from django.contrib import admin
from accounts.models import CustomUser, Profile


class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "date_joined",
        "last_login",
        "is_active",
    )
    list_display_links = ("email",)
    search_field = ("email", "phone_number")
    readonly_fields = ("id", "date_joined", "last_login")


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)

