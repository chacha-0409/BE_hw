from django.db import models

class Phone(models.Model):
    name=models.CharField(max_length=10)
    phone_num=models.CharField(max_length=11)
    email=models.EmailField()
    create_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name