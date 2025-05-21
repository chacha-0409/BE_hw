from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class SignUpForm(UserCreationForm):
    class Meta:
        model = get_user_model() # 현재 프로젝트에서 설정된 사용자 모델 반환 - AUTH_USER_MODEL = '앱이름.모델이름' 전제
        fields = ['university', 'email', 'nickname', 'username']