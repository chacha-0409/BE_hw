from django.db import models
from users.models import User

class Category(models.Model):
    name=models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True, null=True)
    # slug

class Post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    author=models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='posts') # 네임 주의
    is_anonymous=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    category=models.ManyToManyField(to=Category, through="PostCategory", related_name="posts")
    like = models.ManyToManyField(to=User, through='Like', related_name="like_posts")
    scrap = models.ManyToManyField(to=User, through='Scrap', related_name='scrap_posts')

    def __str__(self):
        return f'[{self.id}] {self.title}'

class PostCategory(models.Model):
    post=models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="post_category")
    category=models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name="category_post")

class Like(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='user_likes')
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='post_likes')

class Scrap(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='user_scraps')
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='post_scraps')


class Comment(models.Model):
    post=models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="comments")
    content=models.TextField()
    author=models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='comments')
    is_anonymous=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'[{self.id}] {self.content}'