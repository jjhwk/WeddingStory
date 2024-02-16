from django.contrib import admin
from review.models import Post

@admin.register(Post)
class ReviewAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user_id",
        "title",
        "created_at"
    ]

# Register your models here.
