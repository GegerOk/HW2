from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def base(request):
    return render(request, 'task4/menu.html')
    

def cats_page(request):
    cats = ['f cat', 's cat']
    context = {'cats' : cats
               }
    return render(request, 'task4/cats_page.html', context)
def trash_page(request):
    return render(request, 'task4/trash_page.html')