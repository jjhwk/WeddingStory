from django.contrib import admin
from review.models import Post, Comment
from picture.models import PostImage
from picture.admin import PostImageInline

@admin.register(Post)
class ReviewAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user_id",
        "title",
        "created_at",
        "updated_at",
    ]
    inlines = [

        PostImageInline,
 
    ]

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "post",
        "photo",
    ]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "post",
        "content",
        "created_at",
        "updated_at",
    ]

# Register your models here.
