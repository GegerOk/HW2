from django.shortcuts import render
from django.http import HttpResponse
from task5.form import UserRegister

users = ['user1', 'user2', 'user3']
info = {}


def reg_html(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        print(username, password, repeat_password, age)
        if password != repeat_password:
                info['err_pas'] = "Пароли не совпадают!"
                return render(request, 'task5/registration_page.html', {'info': info})
        if int(age) <= 18:
            info['err_age'] = 'Вы должны быть старше 18'
            return render(request, 'task5/registration_page.html', {'info': info})
        if username in users:
            info['err_name'] = 'Пользователь с таким ником существует'
            return render(request, 'task5/registration_page.html', {'info': info})
        return HttpResponse(f'Приветствуем, {username}!')
    return render(request, 'task5/registration_page.html')


def reg_django(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password != repeat_password:
                    info['err_pas'] = "Пароли не совпадают!"
                    return render(request, 'task5/registration_page.html', {'info': info})
            if int(age) <= 18:
                info['err_age'] = 'Вы должны быть старше 18'
                return render(request, 'task5/registration_page.html', {'info': info})
            if username in users:
                info['err_name'] = 'Пользователь с таким ником существует'
                return render(request, 'task5/registration_page.html', {'info': info})
            return HttpResponse('Регистрация прошла успешно!')
    else:
        form = UserRegister()

    return render(request, 'task5/registration_page2.html', {'form': form})
