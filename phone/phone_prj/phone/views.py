from django.shortcuts import render, redirect, get_object_or_404
from .models import Phone
from django.views.generic import ListView

class IndexView(ListView):
    queryset=Phone.objects.all().order_by('name')
    template_name='phone/list.html'
    context_object_name='phones'

def result(request):
    keyword = request.GET.get('keyword')
    phones = Phone.objects.filter(name__contains=keyword).order_by('name')
    return render(request, 'phone/result.html', {'phones' : phones,'keyword' : keyword})
  
def create(request):
    if request.method=="POST":
        title = request.POST.get('title')
        number = request.POST.get('number')
        email = request.POST.get('email')

        post=Phone.objects.create(
            name=title,
            phone_num=number,
            email=email
        )
        return redirect('phone:list')
    return render(request, 'phone/create.html')

def detail(request, id):
    phone = get_object_or_404(Phone, id=id)
    return render(request, 'phone/detail.html', {'phone':phone})

def update(request, id):
    phone=get_object_or_404(Phone,id=id)

    if request.method=="POST":
        title = request.POST.get('title')
        number = request.POST.get('number')
        email = request.POST.get('email')

        phone.name = title
        phone.phone_num = number
        phone.email = email
        phone.save()
        return redirect('phone:detail', id)
    return render(request, 'phone/update.html', {'phone':phone})

def delete(request, id):
    phone= get_object_or_404(Phone,id=id)
    if request.method == "POST":
        phone.delete()
        return redirect('phone:list')
    return render(request, 'phone/delete.html', {'phone':phone})