from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import ProUser

# Custom User Admin
class ProUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'position')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name','username', 'password1', 'password2', 'position','email'),
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'position')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)

# Unregister the default User admin
admin.site.unregister(User)

# Register the custom user admin
admin.site.register(ProUser, ProUserAdmin)