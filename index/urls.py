from django.urls import path
from index import views

app_name = "index"
urlpatterns = [    
    path("", views.index,name="index"),
    path("map/", views.map, name="map"),
]
