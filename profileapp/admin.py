from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, AbstractUser

from .models import Profile


# Register your models here.

# class ProfileInline(admin.StackedInline):
#     model = Profile
#     can_delete = False
#     verbose_name = '프로필'
#
# class ProfileAdmin(UserAdmin):
#     list_display = ('nickname')
#     inlines= (ProfileInline, )
#
# # admin.site.unregister(AbstractUser)
# admin.site.register(Profile, ProfileAdmin)