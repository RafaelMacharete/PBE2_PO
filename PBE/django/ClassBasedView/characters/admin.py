from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, Character

class AccountAdmin(UserAdmin):
    list_display = ['username', 'is_active', 'profile_image']

    fieldsets = UserAdmin.fieldsets + (
        ('New Fields', 
         {
          'fields': ['username', 'is_active', 'profile_image'],   
         },
         ),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('New Fields', 
         {
          'fields': ['username', 'is_active', 'profile_image'],   
         },
         ),
    )

admin.site.register(Account, AccountAdmin)
admin.site.register(Character)