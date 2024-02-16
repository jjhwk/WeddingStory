from django.shortcuts import render, redirect, get_object_or_404
from users.forms import LoginForm, SignupForm
from django.contrib.auth import authenticate, login, logout
from users.models import User
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse
from django.contrib.auth import get_user_model
# from .models import Profile
# from django.views.generic.detail import DetailView
# from django.views import View
# from .forms import UserForm, ProfileForm


def signup(request):
    if request.method == 'POST':
        
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                                            user_id=request.POST['username'],
                                            password=request.POST['password1'],
                                            email=request.POST['email'],
                                            name=request.POST['name']
                                            )
            login(request, user)
            return redirect('/')
   
    return render(request, "users/signup.html")



def user_login(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        print("id",username)
        print("pw",password)

        user = authenticate(request, user_id=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            
            return render(request, 'users/login.html', {'error' : '아이디 혹은 비밀번호가 틀립니다'})
        
    return render(request, 'users/login.html')

def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')
    return render(request, 'users/login.html') 



def detail(request, pk):
    User = get_user_model()
    user = get_object_or_404(User, pk=pk)
    context = {
        'user': user,

 }
    return render(request, 'users/detail.html', context)


# class ProfileUpdateView(View): # 간단한 View클래스를 상속 받았으므로 get함수와 post함수를 각각 만들어줘야한다.
#     # 프로필 편집에서 보여주기위한 get 메소드
#     def get(self, request):
#         user = get_object_or_404(User, pk=request.user.pk)  # 로그인중인 사용자 객체를 얻어옴
#         user_form = UserForm(initial={
#             'first_name': user.first_name,
#             'last_name': user.last_name,
#         })

#         if hasattr(user, 'profile'):  # user가 profile을 가지고 있으면 True, 없으면 False (회원가입을 한다고 profile을 가지고 있진 않으므로)
#             profile = user.profile
#             profile_form = ProfileForm(initial={
#                 'nickname': profile.nickname,
#                 'profile_photo': profile.profile_photo,
#             })
#         else:
#             profile_form = ProfileForm()

#         return render(request, 'kilogram/profile_update.html', {"user_form": user_form, "profile_form": profile_form})

