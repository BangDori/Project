from django.db import models

from bangdori.models import CustomerUser


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(CustomerUser, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=20, unique=True, null=True)