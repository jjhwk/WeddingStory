from django.urls import path
from users import views


app_name = "users"
urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"), 
    path("signup/", views.signup, name="signup"),
    path("detail/<int:pk>/", views.detail, name="detail"),
]