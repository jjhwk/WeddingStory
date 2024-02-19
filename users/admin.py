from django.contrib import admin
from users.models import User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "user_id",
        "name"
    ]

# class ProfileInline(admin.StackedInline): 
#     model = Profile
#     con_delete = False  