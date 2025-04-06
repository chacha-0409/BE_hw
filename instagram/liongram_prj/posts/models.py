from django.db import models

class Post(models.Model):
    title=models.CharField(max_length=20)
    content=models.TextField()
    views=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def increase_view(self):
        self.views +=1
        self.save()