from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import CustomerUser


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('userid', 'email', 'passwd', 'birthday', 'phone')

admin.site.register(CustomerUser, UserAdmin)