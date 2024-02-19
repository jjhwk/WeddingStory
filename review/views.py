from django.shortcuts import render, redirect, get_object_or_404
from review.models import Post, Comment, PostImage
from review.forms import PostForm, CommentForm
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse
from django.contrib import messages


# Create your views here.
def feed_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    Post.objects.filter(id=post_id).update(view = post.view+1)
    post = Post.objects.get(id=post_id)
    
    comment_form = CommentForm()
    context = {
       "post" : post,
       "comment_form" : comment_form        
    }
    return render(request, "reviews/feed_detail.html", context)

def feeds_list(request):
    posts = Post.objects.all().order_by("-pk")
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

            for image_file in request.FILES.getlist("images"):
                # request.FILES 또는 request.FILES.getlist() 로 가져온 파일은
                # Model 의 ImageField부분에 곧바로 할당
                PostImage.objects.create(
                    post=post,
                    photo=image_file,
                )

            # 피드페이지로 이동하여 생성된 Post의 위치로 스크롤 되도록 함
            url = reverse("reviews:feeds_list") + f"#post-{post.id}"
            return HttpResponseRedirect(url)

    else:       
        form = PostForm()  # class는 변수에 담아줘야 저장 해줌
    context = {"form": form} 
    return render(request, "reviews/feed_add.html", context)

def feed_delete(request, post_id):
    post = Post.objects.get(id=post_id)
    if post.user == request.user:
        post.delete()
        return redirect("reviews:feeds_list")
    else:
        return HttpResponseForbidden("이 댓글을 삭제할 권한이 없습니다")
    
def feed_update(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    print(post.content)
    if post.user != request.user:
        messages.error(request, '수정권한이 없습니다')
        return redirect('reviews:feed_detail', post_id=post.id)
    
    if request.method == "POST":
        print(request.POST)
        # form = PostForm(request.POST, instance=post)
        print(request.POST)
        
        Post.objects.create(
            id=post_id,
            title=request.POST["title"],
            content = request.POST["content"],      
            score = request.POST["score"]          
        )
        url = reverse('reviews:feed_detail')+"/"+post.id+"/"
        print(url)
        return redirect('reviews:feed_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)
        context = { 'form': form,
                'post':post
            }
        return render(request, 'reviews/feed_update.html', context)
    

def feed_update_page(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    print(post)
    if request.method == "POST":
        
        form = PostForm(instance=post)
        context = {
                'post':post
            }
        return render(request, 'reviews/feed_update.html', context)


@require_POST # 댓글 작성을 처리할 View, Post 요청만 허용
def comment_add(request, post_id):
    # request.POST 로 전달된 데이터를 사용해 CommentForm 인스턴스를 생성
    form = CommentForm(data=request.POST)

    if form.is_valid():
        # commit=False 옵션으로 메모리상에 Comment 객체 생성
        comment = form.save(commit=False)

        # Comment 생성에 필요한 사용자 정보를 request에서 가져와 할당
        comment.user = request.user

        # DB에 Comment 객체 저장
        comment.save()
       
        # URL 로 'next'값을 전달받았다면 댓글 작성 완료 후 전달받은 값으로 이동
        if request.GET.get("next"):
            url_next = request.GET.get("next")

        else: # "next"값을 전달받지 않았다면 피드페이지의 글 위치로 이동
            # 생성한 comment에서 연결된 post 정보를 가져와서 id값을 사용
            url_next = reverse("reviews:feeds_list") + f"#post-{comment.post.id}"
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
