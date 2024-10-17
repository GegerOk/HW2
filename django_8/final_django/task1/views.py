from os import name
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView
from task1.form import UserRegister
from django.http import HttpResponse
from task1.models import *

info = {}


# Create your views here.
def base(request):
    return render(request, 'task1/menu.html')
    

def game_page(request):
    games = Game.objects.all()
    return render(request, 'task1/game_page.html', {'Games': games})
def trash_page(request):
    return render(request, 'task1/trash_page.html')

def reg_html(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        print(username, password, repeat_password, age)
        if password != repeat_password:
                info['err_pas'] = "Пароли не совпадают!"
                return render(request, 'task1/registration_page.html', {'info': info})
        if int(age) <= 18:
            info['err_age'] = 'Вы должны быть старше 18'
            return render(request, 'task1/registration_page.html', {'info': info})
        for i in Buyer.objects.all():
            if username == i.name:
                info['err_name'] = 'Такой пользователь уже существует'
                return render(request, 'task1/registration_page.html', {'info': info})
        Buyer.objects.create(name=username, balance=0, age=age)
        return HttpResponse(f'Приветствуем, {username}!')
    return render(request, 'task1/registration_page.html')
