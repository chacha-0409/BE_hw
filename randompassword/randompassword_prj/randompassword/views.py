from django.shortcuts import render
import string
import random

# Create your views here.

def index(request):
    return render(request,'index.html')

def password_generator(request):
    length=request.GET.get('length') # 선택>True
    upper="upperAlphabet" in request.GET
    lower="lowerAlphabet" in request.GET
    digits="number" in request.GET
    special='special' in request.GET

    # 비밀번호 입력 판별
    try:
        length=int(length)
    except ValueError:
        return render(request,'error2.html')

    # 비밀번호가 음수일 때
    if length<0:
        return render(request,'error1.html')
    
    # 옵션을 선택하지 않았을 때
    elif not (upper or lower or digits or special):
        return render(request,'error3.html')

    #문자 set 구성
    check_chars = ""
    if upper:
        check_chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #string.ascii_uppercase
    if lower:
        check_chars += "abcdefghijklmnopqrstuvwxyz"
    if digits:
        check_chars += "0123456789"
    if special:
        check_chars += "!@#$%^&*"

    check_chars=list(check_chars)
    password=''.join([random.choice(check_chars) for i in range(length)])

    return render(request,'result.html',{'password':password})

