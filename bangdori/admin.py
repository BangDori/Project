from django.contrib import admin

from .models import CustomerUser
from .models import Authentication


class UserAdmin(admin.ModelAdmin):
<<<<<<< HEAD




    list_display = ('username', 'email', 'password', 'birthday', 'phone')
=======
    list_display = ('username', 'email', 'password', 'birthday', 'phone', 'nickname')
>>>>>>> 21cd9f66711fe615fc1112a1646e1fb5e7b0552a



class SMSAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'auth_number')


admin.site.register(Authentication, SMSAdmin)
admin.site.register(CustomerUser, UserAdmin)
