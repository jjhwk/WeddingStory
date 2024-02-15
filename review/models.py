from django.db import models

# Create your models here.
class Post(models.Model):    
    title = models.CharField("포스트 제목", max_length=100)
    user_id = models.ForeignKey("users.User", verbose_name="작성자", on_delete=models.CASCADE)
    content = models.TextField("포스트 내용")
    created_at = models.DateTimeField("작성일시", auto_now_add=True) 
    updated_at = models.DateTimeField("글수정시간", auto_now=True)
    view = models.PositiveIntegerField(default=0)
    

    def __str__(self):       # 제목을 문자열로 보여쥼 
        return self.title
     
