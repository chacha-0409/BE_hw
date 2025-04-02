from django.db import models
#모델은 모두 django.models.Model의 서브클래스

class Post(models.Model): #상속x
    title=models.CharField(max_length=50)
    content=models.TextField()
    create_at=models.DateTimeField(auto_now_add=True)

    def __str__(self): #객체를 호출하면 자동 실행
        return self.title

# Create your models here.
