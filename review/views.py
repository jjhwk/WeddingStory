from django.shortcuts import render, redirect, get_object_or_404
from review.models import Post, Comment
from review.forms import PostForm, CommentForm
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse


# Create your views here.
def feed_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
       "post" : post,        
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


@require_POST # 댓글 작성을 처리할 View, Post 요청만 허용
def comment_add(request):
    # request.POST 로 전달된 데이터를 사용해 CommentForm 인스턴스를 생성
    form = CommentForm(data=request.POST)

    if form.is_valid():
        # commit=False 옵션으로 메모리상에 Comment 객체 생성
        comment = form.save(commit=False)

        # Comment 생성에 필요한 사용자 정보를 request에서 가져와 할당
        comment.user = request.user

        # DB에 Comment 객체 저장
        comment.save()
       
        # URL 로 'next'값을 전달받았다면 댓글 작성 완료 후 전당받은 값으로 이동
        if request.GET.get("next"):
            url_next = request.GET.get("next")

        else: # "next"값을 전달받지 않았다면 피드페이지의 글 위치로 이동
            # 생성한 comment에서 연결된 post 정보를 가져와서 id값을 사용
            url_next = reverse("posts:feeds") + f"#post-{comment.post.id}"
        return HttpResponseRedirect(url_next)


@require_POST
def comment_delete(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if comment.user == request.user:
        comment.delete()
        url = reverse("reviews:feeds_list") + f"#post-{comment.post.id}"
        return HttpResponseRedirect(url)
    else:
        return HttpResponseForbidden("이 댓글을 삭제할 권한이 없습니다")    
