from django.contrib import admin
from review.models import Post, Comment, PostImage

class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1

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
