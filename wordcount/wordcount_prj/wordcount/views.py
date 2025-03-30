from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def word_count(request):
    return render(request,'word_count.html')

def result(request):
    entered_text=request.GET['fulltext']
    word_list=entered_text.split()
    word_count=len(word_list) # 1. 단어 개수 리스트 길이

    word_dictionary={}

    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word]+=1
        else:
            word_dictionary[word]=1

    # 3. 글자 수 세기 기능 추가
    most_word_count=max(word_dictionary.values())
    most_word = [word for word, count in word_dictionary.items() if count == most_word_count]
    
    ch_count=len(entered_text)
    ch_count_noblank=len(entered_text.replace(" ",""))
    
    return render(request,'result.html', {'alltext':entered_text, 
    'dictionary':word_dictionary.items(), 
    'word_count':word_count, # 1. 단어 개수 리턴
    'most_word':most_word, # 3. 글자 수 새기
    'most_word_count':most_word_count,
    'ch_count_noblank':ch_count_noblank,
    'ch_count':ch_count,
    })
    
# 4. hello.html에서 이름 출력

def hello(request):
    name=request.GET['name']
    return render(request,'hello.html',{'name':name, 'month':month, 'year':year, 'day':day})
    