from django.shortcuts import render, redirect, get_object_or_404
from users.forms import LoginForm, SignupForm
from django.contrib.auth import authenticate, login, logout
from users.models import User
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    AuthenticationForm,
    PasswordChangeForm,
)



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



def update(request):
    if request.method == "POST":
    	# updating
        user_change_form = UserChangeForm(data=request.POST, instance=request.user)
        
        if user_change_form.is_valid() and profile_form.is_valid():
            user = user_change_form.save()
        
    else:
        # editting
        user_change_form = UserChangeForm(instance=request.user)

        context = {
            'user_change_form': user_change_form,
        }
        
        return render(request, 'users/update.html', context)