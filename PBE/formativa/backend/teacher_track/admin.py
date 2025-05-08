from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, Classroom, Subject

class AccountAdmin(UserAdmin):
    list_display = ('username', 'name', 'phone')
    fieldsets = UserAdmin.fieldsets + (
        (None, 
            {'fields': ('name', 'phone')}
            ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None,
         {'fields': ('name', 'phone', 'profile_picture')}),
    )
    
admin.site.register(Classroom)
admin.site.register(Subject)
admin.site.register(Account, AccountAdmin)