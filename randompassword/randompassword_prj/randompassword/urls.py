from django.urls import path
from .views import *

app_name='randompassword'

urlpatterns = [
    path('', index, name="index"),
    path('result/', password_generator, name="result"),
]