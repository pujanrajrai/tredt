from distutils.command import upload
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    phone_number = models.IntegerField(blank=True,null=True)
    photo=models.ImageField(upload_to="profile/pic/",verbose_name="Your Photo")
