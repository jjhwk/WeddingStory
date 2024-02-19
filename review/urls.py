from django.urls import path
from review import views

app_name = "reviews"
urlpatterns = [
    path("", views.feeds_list, name = "feeds_list"),
    path("<int:post_id>/", views.feed_detail, name = "feed_detail"),
    path("feed_add/", views.feed_add, name = "feed_add"),
    path("feed_delete/<int:post_id>/", views.feed_delete, name = "feed_delete"),
    path("<int:post_id>/feed_update/", views.feed_update, name = "feed_update"),
    path("feed_update/<int:post_id>/", views.feed_update, name = "feed_update_page"),
    path("<int:post_id>/comment_add/", views.comment_add, name="comment_add"),
    path("comment_delete/<int:comment_id>/", views.comment_delete, name="comment_delete"),
]
