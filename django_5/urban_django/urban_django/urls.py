"""
URL configuration for urban_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from task4.views import base, cats_page, trash_page
from task5.views import reg_django, reg_html

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cats_page', cats_page),
    path('base', base),
    path('trash_page', trash_page ),
    path('registration_page/', reg_html),
    path('registration_page_2/', reg_django),
    
]