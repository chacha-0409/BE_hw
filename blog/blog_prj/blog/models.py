from django.db import models
#모델은 모두 django.models.Model의 서브클래스
from users.models import User

class Category(models.Model):
    name=models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return self.name

class Post(models.Model): #상속
    title=models.CharField(max_length=50)
    content=models.TextField()
    create_at=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='posts')
    category=models.ManyToManyField(to=Category, through="PostCategory", related_name="posts")
    like = models.ManyToManyField(to=User, through="Like", related_name="like_posts")

    def __str__(self): #객체를 호출하면 자동 실행
        return f'[{self.id}] {self.title}'


class Comment(models.Model): # 다대일-댓글
    post=models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="comments")
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f'[{self.id}] {self.content}'

class PostCategory(models.Model): #중간테이블 v foreignkey만 있음 > add remove 메서드 사용가능
    post=models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="post_category")
    category=models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name="post_category")

class Like(models.Model):
    user=models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="user_likes")
    post=models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="post_likes")