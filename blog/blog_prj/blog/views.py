from django.shortcuts import render, redirect
from .models import Post, Comment, Category
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

def list(request):
    categories=Category.objects.all()
    category_id=request.GET.get('category')
    
    if category_id:
        category=get_object_or_404(Category, id=category_id) # 용자가 URL 쿼리로 넘긴 category_id 값을 기반으로, 해당하는 Category 모델의 객체가 존재하면 가져옴
        # 정참조
        # posts=category.posts.all().order_by('-id')
        # filter 메서드
        posts=Post.objects.filter(category=category).order_by('-id') # 필드=객체
    else:
        posts=Post.objects.all().order_by('-id')
    
    return render(request,'blog/list.html',{'posts': posts, 'categories':categories})

@login_required
def create(request):
    categories=Category.objects.all()
    if request.method=="POST":
        title = request.POST.get('title')
        content = request.POST.get('content')

        category_ids=request.POST.getlist('category')  # 모델-category 
        category_list=[get_object_or_404(Category, id=category_id) for category_id in category_ids]

        image = request.FILES.get('image')
        video = request.FILES.get('video')
        print(image)

        post=Post.objects.create(
            title=title,
            content=content,
            author=request.user,
            image = image,
            video = video,
        )

        for category in category_list:
            post.category.add(category)

        return redirect('blog:list')
    return render(request, 'blog/create.html', {'categories':categories})

def detail(request, id):
    post = get_object_or_404(Post,id=id)
    return render(request, 'blog/detail.html', {'post':post})

def update(request, id):
    post = get_object_or_404(Post,id=id)

    if request.method=='POST':
        post.title=request.POST.get('title')
        post.content=request.POST.get('content')
        image = request.FILES.get('image')
        video = request.FILES.get('video')
        print(image)

        if image:
            post.image.delete()
            post.image = image
        if video:
            post.video.delete()
            post.video = video
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

def like(request, post_id):
    post=get_object_or_404(Post, id=post_id)
    user=request.user
    ''' 정참조
    if user in post.like.all(): # 좋아요 있으면
        post.like.remove(user)
    else:
        post.like.add(user)
    return redirect('blog:detail', post_id)
    '''
    # 역참조
    if post in user.like_posts.all():
        post.like.remove(user)
    else:
        post.like.add(user)
    return redirect('blog:detail', post_id)
    