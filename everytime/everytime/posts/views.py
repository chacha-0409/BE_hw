from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def main(request):
    categories = Category.objects.all()

    category_posts = {}

    for category in categories:
        posts = category.posts.order_by('-created_at')[:4]
        category_posts[category] = posts

    return render(request, 'posts/main.html', {'categories':categories, 'category_posts':category_posts})

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        is_anonymous = 'is_anonymous' in request.POST
        image = request.FILES.get('image')
        video = request.FILES.get('video')

        post = Post.objects.create(
            title = title,
            content = content,
            is_anonymous = is_anonymous,
            author = request.user,
            image = image,
            video = video
        )

        PostCategory.objects.create(
            post = post,
            category = category
        )
        return redirect('posts:category', slug=slug)
    
    posts = category.posts.all().order_by('-created_at')
    return render(request, 'posts/category.html', {'category': category, 'posts':posts})

def detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'posts/detail.html', {'post':post})

def create_comment(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        content = request.POST.get('content')
        is_anonymous = 'is_anonymous' in request.POST

        Comment.objects.create(
            post=post,
            content = content,
            author = request.user,
            is_anonymous = is_anonymous,
        )
        return redirect('posts:detail', post.id)
    
def delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('posts:main')

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    post_id = comment.post.id
    comment.delete()
    return redirect('posts:detail', post_id)

def update(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.is_anonymous = 'is_anonymous' in request.POST
        image = request.FILES.get('image')
        video = request.FILES.get('video')

        if image:
            post.image.delete()
            post.image = image
        
        if video:
            post.video.delete()
            post.video = video
            
        post.save()
        return redirect('posts:detail', id)
    return render(request, 'posts/update.html', {'post':post})

def like(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        user = request.user

        if user in post.like.all():
            post.like.remove(user)
        else:
            post.like.add(user)
    
    return redirect('posts:detail', post_id)

def scrap(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        user = request.user

        if user in post.scrap.all():
            post.scrap.remove(user)
        else:
            post.scrap.add(user)
    
    return redirect('posts:detail', post_id)