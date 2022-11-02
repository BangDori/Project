from django.contrib import admin

from .models import CustomerUser
from .models import Authentication

# Register your models here.


class UserAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ('username', 'email', 'password', 'birthday', 'phone')
=======
<<<<<<< HEAD
    list_display = ('username', 'email', 'password', 'birthday', 'phone', 'nickname')
=======
    list_display = ('username', 'email', 'password', 'birthday', 'phone','nickname')
>>>>>>> 1156ba765b0c3afabe30ee719ac3ef0204e2f9c5
>>>>>>> 2f71611ec921cc5e5e5e76a0ae0d74c53bc3f202


class SMSAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'auth_number')


admin.site.register(Authentication, SMSAdmin)
admin.site.register(CustomerUser, UserAdmin)
