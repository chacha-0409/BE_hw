from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.views.generic import ListView
from django.db.models import Q

class IndexView(ListView):
    queryset=Post.objects.all().order_by('-id')
    template_name='posts/list.html'
    context_object_name='posts'

def result(request):
    keyword = request.GET.get('keyword')
    posts = Post.objects.filter(Q(title__contains=keyword)|Q(content__contains=keyword)).order_by('created_at')
    return render(request, 'posts/result.html', {'posts' : posts,'keyword' : keyword})
  
def create(request):
    if request.method=="POST":
        title = request.POST.get('title')
        content = request.POST.get('content')

        post=Post.objects.create(
            title=title,
            content=content
        )
        return redirect('posts:list')
    return render(request, 'posts/create.html')

def detail(request, id):
    post = get_object_or_404(Post, id=id)
    post.increase_view()
    return render(request, 'posts/detail.html', {'post' : post})

def update(request, id):
    post=get_object_or_404(Post,id=id)

    if request.method=="POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        post.title = title
        post.content = content
        post.save()
        return redirect('posts:detail', id)
    return render(request, 'posts/update.html', {'post':post})

def delete(request, id):
    post= get_object_or_404(Post,id=id)
    post.delete()
    return redirect('posts:list')