from django.shortcuts import render, redirect
from .models import Post, Comment
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

def list(request):
    posts = Post.objects.all().order_by('-id')
    return render(request,'blog/list.html',{'posts': posts})

@login_required
def create(request):
    if request.method=="POST":
        title = request.POST.get('title')
        content = request.POST.get('content')

        post=Post.objects.create(
            title=title,
            content=content,
            author=request.user,
        )
        return redirect('blog:list')
    return render(request, 'blog/create.html')

def detail(request, id):
    post = get_object_or_404(Post,id=id)
    return render(request, 'blog/detail.html', {'post':post})

def update(request, id):
    post = get_object_or_404(Post,id=id)

    if request.method=='POST':
        post.title=request.POST.get('title')
        post.content=request.POST.get('content')
        post.save()
        return redirect('blog:detail', id)
    return render(request, 'blog/update.html', {'post':post})

def delete(request, id):
    post= get_object_or_404(Post,id=id)
    post.delete()
    return redirect('blog:list')


@login_required
def create_comment(request, post_id):
    post=get_object_or_404(Post, id=post_id)
    if request.method=='POST':
        content=request.POST.get('content')

        Comment.objects.create(
            post=post,
            content=content,
            author=request.user
        )
        return redirect('blog:detail', post_id)
    return redirect('blog:list')

