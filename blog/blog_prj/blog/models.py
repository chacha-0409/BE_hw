from django.db import models
#모델은 모두 django.models.Model의 서브클래스
from users.models import User

class Post(models.Model): #상속
    title=models.CharField(max_length=50)
    content=models.TextField()
    create_at=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self): #객체를 호출하면 자동 실행
        return f'[{self.id}] self.title'


class Comment(models.Model): # 다대일-댓글
    post=models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="comments")
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f'[{self.id}] {self.content}'