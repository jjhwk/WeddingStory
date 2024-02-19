from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import User


# Create your models here.
class Post(models.Model):  
    user = models.ForeignKey(User, verbose_name="사용자 아이디", on_delete=models.CASCADE)  
    title = models.CharField("포스트 제목", max_length=100)
    content = models.TextField("포스트 내용") 
    created_at = models.DateTimeField("작성 일시", auto_now_add=True) 
    updated_at = models.DateTimeField("글수정 시간", auto_now=True)
    view = models.IntegerField(default=0)
    score = models.IntegerField("평점", validators=[MinValueValidator(0), MaxValueValidator(5)])


    
    def __str__(self):       # 제목을 문자열로 보여쥼 
        return self.title
    def __str__(self):
        return f"{self.user.user_id}의 Post(id:{self.id})"
    

class Comment(models.Model):
    user = models.ForeignKey("users.User", verbose_name="사용자 아이디", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name="포스트", on_delete=models.CASCADE)
    content = models.TextField("내용")
    created_at = models.DateTimeField("작성일시", auto_now_add=True)
    updated_at = models.DateTimeField("글수정 시간", auto_now=True)

    def __str__(self):
        return self.content
    
class PostImage(models.Model):
    post = models.ForeignKey("review.Post", verbose_name="포스트", on_delete=models.CASCADE)
    photo = models.ImageField("사진", upload_to="post")
