from django.contrib import admin

from .models import CustomerUser


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'password', 'birthday', 'phone')


admin.site.register(CustomerUser, UserAdmin)
