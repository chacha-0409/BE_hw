from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

def signup(request):
    if request.method == 'GET':
        form = SignUpForm()
        return render(request, 'accounts/signup.html', {'form': form})

    form = SignUpForm(request.POST) # 모델과 연결된 ModelForm 기반의 사용자 정의 폼
    if form.is_valid():
        form.save()
        return redirect('accounts:login')
    else:
        return render(request, 'accounts/signup.html', {'form': form})

def login(request):
    if request.method == 'GET':
        return render(request, 'accounts/login.html', {'form':AuthenticationForm()})

    form = AuthenticationForm(request, request.POST) # Django에서 제공하는 로그인 폼
    if form.is_valid():
        auth_login(request, form.user_cache) 
        return redirect('posts:main')

    return render(request, 'accounts/login.html', {'form': form})

def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        return redirect('posts:main')

def mypage(request):
    return render(request, 'accounts/mypage.html')

def user_info(request):
    return render(request, 'accounts/user_info.html')

def myblog(request):
    posts=request.user.posts.all().order_by('-id')
    return render(request, 'accounts/myblog.html', {'posts':posts})


def mypost(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'accounts/mypost.html', {'posts':posts})
