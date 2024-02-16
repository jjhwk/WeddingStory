from django.urls import path
from review import views

app_name = "reviews"
urlpatterns = [
    path("", views.feeds_list, name = "feeds_list"),
    path("<int:post_id>/", views.feed_detail, name = "feed_detail"),
    path("feed_add/", views.feed_add, name = "feed_add"),
    path("<int:post_id>/comment_add/", views.comment_add, name="comment_add"),
    path("comment_delete/<int:comment_id>/", views.comment_delete, name="comment_delete"),
]