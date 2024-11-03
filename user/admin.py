from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = (
        'first_name',
        'last_name',
        'username',
        'email',
        'is_staff',
        'is_superuser'
    )
    list_filter = ('is_staff', 'is_superuser')
    search_fields = ('first_name', 'last_name', 'username', 'email')
    list_per_page = 10
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'For Activity',
            {
                'fields': (
                    'last_active_datetime',
                )
            }
        ),
        (
            'For Orders and Contacting',
            {
                'fields': (
                    'order_address',
                    'city',
                    'country',
                    'postcode',
                    'mobile'
                )
            }
        )
    )
