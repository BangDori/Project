from django.contrib import admin

from .models import CustomerUser
from .models import Authentication

# Register your models here.


class UserAdmin(admin.ModelAdmin):
<<<<<<< HEAD

    list_display = ('username', 'email', 'password', 'birthday', 'phone')


=======
    list_display = ('username', 'email', 'password', 'birthday', 'phone')
>>>>>>> 5fb3e6ddd4a68a6d85ef8a1e8eab9d39cd35ad5d


class SMSAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'auth_number')


admin.site.register(Authentication, SMSAdmin)
admin.site.register(CustomerUser, UserAdmin)
