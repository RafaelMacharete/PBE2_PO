from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

class AccountAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        (None,
         {'fields': ('biography',
                    'age', 
                    'phone_number', 
                    'address', 
                    'education', 
                    'animal_quantity')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None,
         {'fields': ('biography', 
                    'age', 
                    'phone_number', 
                    'address', 
                    'education', 
                    'animal_quantity')}),    
    )
admin.site.register(Account, AccountAdmin)
