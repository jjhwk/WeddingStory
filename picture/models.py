from django.db import models
from review.models import Post

# Create your models here.

class PostImage(models.Model):
    post = models.ForeignKey(Post,
                             verbose_name="포스트",
                             on_delete=models.CASCADE)
    photo = models.ImageField("사진", upload_to="post")