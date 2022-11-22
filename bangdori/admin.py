from django.contrib import admin

from .models import CustomerUser
from .models import Authentication

# Register your models here.


class UserAdmin(admin.ModelAdmin):

    list_display = ('username', 'email', 'password', 'birthday', 'phone')


<<<<<<< HEAD

=======
>>>>>>> df5475664ccedc2d607345c595fa3c71409a0e44
class SMSAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'auth_number')


admin.site.register(Authentication, SMSAdmin)
admin.site.register(CustomerUser, UserAdmin)