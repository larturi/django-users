from django.contrib import admin

from .models import User
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'username',
        'email',
        'gender',
        'is_staff',
    )

    search_fields = ('first_name', 'last_name', 'username')
    list_filter = ('gender',)

admin.site.register(User, UserAdmin)
