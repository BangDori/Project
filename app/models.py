from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomerUser(models.Model):

    userid = models.CharField(max_length=50, db_column='userid', verbose_name='userid')
    passwd = models.CharField(max_length=50, db_column='passwd', verbose_name='passwd')
    email = models.CharField(max_length=30, db_column='email', verbose_name='email', blank=True)
    birthday = models.CharField(default="19001011", max_length=10, db_column='birth', verbose_name='birth')
    phone = models.IntegerField(default=None, db_column='phone', verbose_name='phone')

    def __str__(self):
        return '이름: '+ self.userid + ", 이메일: "+ self.email + "생년월일"+ self.birthday