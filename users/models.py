from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(models.Model):
    user_id = models.CharField("사용자 아이디", unique = True, max_length = 16)
    password = models.CharField("비밀번호", max_length = 20)
    name = models.CharField("이름", max_length = 20)
    user_tel = models.CharField("전화번호", max_length = 11)
    email = models.CharField("이메일", max_length =20)   

