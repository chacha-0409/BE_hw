from django.urls import path
from .views import *

app_name = 'posts'

urlpatterns = [
    path('', main, name='main'),
    path('detail/<int:id>/', detail, name='detail'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
    path('create-comment/<int:id>', create_comment, name='create-comment'),
    path('delete-comment/<int:id>', delete_comment, name='delete-comment'),
]