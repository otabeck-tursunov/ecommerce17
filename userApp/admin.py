from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *


class CustomUserAdmin(UserAdmin):
    fieldsets = [
        ('Auth',
         {'fields':
              ['username', 'password'],
          },
         ),
        ('Details',
         {'fields': ['first_name', 'last_name', 'middle_name', 'email', 'phone_number', 'birth_date', 'gender',
                     'address', 'date_joined'],
          },
         )
    ]


admin.site.register(User, CustomUserAdmin)
