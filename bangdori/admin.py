from django.contrib import admin

from .models import CustomerUser
from .utils import getAllArticleModels


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'password', 'birthday', 'phone')


admin.site.register(CustomerUser, UserAdmin)
admin.site.register([x for x in getAllArticleModels()])