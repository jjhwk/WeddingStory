from django.shortcuts import render, redirect
from review.models import Post, Comment
from review.forms import PostForm, CommentForm
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse


# Create your views here.
def feed_detail(request, post_id):
    posts = Post.objects.get(id=post_id)
    context = {
       "posts" : posts,        
    }
    return render(request, "reviews/feed_detail.html", context)

def feeds_list(request):
    posts = Post.objects.all()
    comment_form =CommentForm()
    context = {
       "posts" : posts,   
       "comment_form":comment_form     
    }
    return render(request, "reviews/feeds_list.html", context)


def feed_add(request):
    if request.method == "POST":
        print(request.user)
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            print(request.user)
            post.user = request.user
            post.save()

            # 피드페이지로 이동하여 생성된 Post의 위치로 스크롤 되도록 함
            url = reverse("reviews:feeds_list") + f"#post-{post.id}"
            return HttpResponseRedirect(url)

    else:       
        form = PostForm()  # class는 변수에 담아줘야 저장 해줌
    context = {"form": form} 
    return render(request, "reviews/feed_add.html", context)

