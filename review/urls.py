from django.urls import path
from review import views

urlpatterns = [
    path("reviews/", views.feeds, name = "feeds"),
]