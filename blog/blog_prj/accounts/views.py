from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login # alias) 설정
from django.contrib.auth import logout as auth_logout

def signup(request):
    if request.method=='GET':
        form=SignUpForm() # 직접 커스텀
        return render(request, 'accounts/signup.html', {'form':form})
    
    form=SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('accounts:login') # name 잘못 써서 오류2
    else:
        return render(request, 'accounts/signup.html',{'form':form})

def login(request):
    if request.method=='GET': # forms로 잘못 써서 오류1
        return render(request, 'accounts/login.html', {'form':AuthenticationForm()})

    form=AuthenticationForm(request, request.POST) # 상속받음음
    if form.is_valid():
        auth_login(request, form.user_cache)
        return redirect('blog:list')
    return render(request, 'accounts/login.html', {'form':form})

def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('blog:list')

def user_info(request):
    return render(request, 'accounts/user_info.html')

def mypage(request):
    return render(request, 'accounts/mypage.html')

def myblog(request):
#    posts = request.user.posts.all().order_by('-id')
    posts = Post.objects.filter(author=request.user).order_by('-id')
    return render(request, 'accounts/myblog.html', {'posts': posts})
