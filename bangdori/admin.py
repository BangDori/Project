from django.contrib import admin

from .models import CustomerUser
from .models import Authentication

# Register your models here.


class UserAdmin(admin.ModelAdmin):
<<<<<<< HEAD

    list_display = ('username', 'email', 'password', 'birthday', 'phone')



=======
    list_display = ('username', 'email', 'password', 'birthday', 'phone')


>>>>>>> ca7534a73ba48553379ea512186b69489dbcbad4
class SMSAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'auth_number')


admin.site.register(Authentication, SMSAdmin)
admin.site.register(CustomerUser, UserAdmin)
