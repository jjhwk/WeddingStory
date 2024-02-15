from django.urls import path
from review import views

app_name = "reviews"
urlpatterns = [
    path("", views.feeds_list, name = "feeds_list"),
    path("<int:post_id>/", views.feed_detail, name = "feed_detail"),
]