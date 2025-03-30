from django.contrib import admin
from django.urls import path, include #include로 url관리

urlpatterns = [
    path('admin/', admin.site.urls),
    path('randompassword/', include('randompassword.urls')),
]