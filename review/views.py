from django.shortcuts import render, redirect
from review.models import Post

# Create your views here.
def feeds(request):
    posts = Post.objects.all()
    context = {
       "posts" : posts,        
    }
    return render(request, "reviews/feeds.html", context)