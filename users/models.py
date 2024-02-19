from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.db import models
from django.utils import timezone

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, user_id, name, email, password):
        """
        주어진 이메일, 닉네임, 비밀번호 등 개인정보로 User 인스턴스 생성
        """
        if not user_id:
            raise ValueError(('Users must have an email address'))

        user = self.model(
            user_id = user_id,
            email = email,
            name = name,
            
            
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, password):
        """
        주어진 이메일, 닉네임, 비밀번호 등 개인정보로 User 인스턴스 생성
        단, 최상위 사용자이므로 권한을 부여한다. 
        """
        user = self.create_user(
            user_id=user_id,
            password=password,
            
        )

        user.is_superuser = True
        user.save(using=self._db)
        return user
class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.CharField("사용자 아이디", unique = True, max_length = 16)    
    name = models.CharField("이름",  max_length = 20)
    user_tel = models.CharField("전화번호",  max_length = 11)
    email = models.EmailField("이메일", max_length =20)   
    objects = UserManager()

    USERNAME_FIELD = 'user_id'
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All superusers are staff
        return self.is_superuser