from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname', 'username', 'email', 'joined_date', 'is_active', 'is_superuser')
    list_editable = ('is_active', 'is_superuser')
    list_display_links = ('username', )


admin.site.register(User, UserAdmin)

