from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator
from datetime import timedelta

def base (request):
    return render(request, 'base.html')

def register(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')
    else:
        form = Registration()

    return render(request, 'registration.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  
                return redirect('posts')
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Неверный логин или пароль.'})
        return render(request, 'login.html', {'form': form, 'error': 'Что-то пошло не так.'})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def posts(request):
    post_list = Post.objects.all().order_by('-created_at')
    paginator = Paginator(post_list, 3) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    posts_per_page = request.GET.get('posts_per_page', 5)
    paginator = Paginator(post_list, posts_per_page)
    page_obj = paginator.get_page(page_number)
    username = request.user.username if request.user.is_authenticated else None
    threshold_time = timezone.now() - timedelta(minutes=1)
    online_users = CustomUser.objects.filter(last_activity__gte=threshold_time)
    return render(request, 'posts.html', {'posts': page_obj, 'posts_per_page': posts_per_page, 'username': username, 'online_users': online_users})

def create_post(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        image = request.FILES.get('image') 
        post = Post(title=title, content=content, image=image, author=request.user)
        post.save()
        return redirect('posts') 
    return render(request, 'new_post.html')
