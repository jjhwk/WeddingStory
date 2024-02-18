from django.contrib import admin
from picture.models import PostImage
import admin_thumbnails
# Register your models here.

@admin_thumbnails.thumbnail("photo")
class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1