import uuid
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils.safestring import mark_safe
from .orders_entity import *
from .products_entity import *


class CustomerProfile(models.Model):
    SEX = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Secret", "Secret"),
    )
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, unique=True)
    avatar = models.ImageField(upload_to="mudi")
    country = models.CharField(max_length=10, default="China")
    gender = models.CharField(max_length=10, null=True, choices=SEX)
    state_or_province = models.CharField(max_length=20, default="Jiangsu")
    city = models.CharField(max_length=20, default="Najing")
    zip_code = models.IntegerField(default=210010)
    address = models.TextField()

    def user_name(self):
        return self.customer.username + '   (' + self.customer.email + ')    ' + self.customer.first_name

    def avatar_preview(self):
        if self.avatar:
            return mark_safe(f'<img src="{self.avatar.url}" style="width: 50px; height:50px; object-fit:contain;" />')
        else:
            return 'No avatar'

    avatar_preview.short_description = "Avatar"
