from django.db import models
from users.models import User

class Post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    author=models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='posts') # 네임 주의
    is_anonymous=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'[{self.id}] {self.title}'


class Comment(models.Model):
    post=models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="comments")
    content=models.TextField()
    author=models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='comments')
    is_anonymous=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'[{self.id}] {self.content}'