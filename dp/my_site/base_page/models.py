from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null = False, blank = False)
    info = models.TextField(null = True, blank = True)
    email = models.EmailField(null = False, blank = False, unique = True)
    username = models.CharField(null = False, blank = False, unique = True, max_length = 32)
    last_activity = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title