from django.shortcuts import render, redirect
from review.models import Post
from review.forms import PostForm
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse


# Create your views here.
def feed_detail(request, post_id):
    posts = Post.objects.get(id=post_id)
    context = {
       "posts" : posts,        
    }
    return render(request, "reviews:feed_detail", context)

def feeds_list(request):
    posts = Post.objects.all()
    context = {
       "posts" : posts,        
    }
    return render(request, "reviews:feeds_list")

def feed_add(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = request.user_id
            post.save()

            # 피드페이지로 이동하여 생성된 Post의 위치로 스크롤 되도록 함
            url = reverse("posts:feeds") + f"#post-{post.id}"
            return HttpResponseRedirect(url)

    else:       
        form = PostForm()  # class는 변수에 담아줘야 저장 해줌
    context = {"form": form} 
    return render(request, "reviews:feed_add", context)        