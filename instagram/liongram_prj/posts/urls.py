from django.urls import path
from .views import *

app_name='posts'

urlpatterns=[
    path('', IndexView.as_view(), name='list'),
    path('create/', create, name='create'),
    path('detail/<int:id>/', detail, name='detail'),
    path('update/<int:id>/', update, name='update'),
    path('delete/<int:id>/', delete, name='delete'),
    path('result/', result, name='result'),
]