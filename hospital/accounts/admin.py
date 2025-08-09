from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'user_type', 'is_staff', 'is_active','profile_picture']
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('user_type','profile_picture')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
