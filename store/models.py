from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(max_length=3, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pic/', blank=True, null= True)
    
