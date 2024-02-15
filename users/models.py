from django.db import models
# from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(models.Model):
    user_id = models.CharField("사용자 아이디", unique = True, max_length = 16)
    


