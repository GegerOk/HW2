from django.db import models

# Create your models here.

class Buyer(models.Model):
    name = models.CharField(max_length=20)
    balance = models.DecimalField(decimal_places=2, max_digits=10)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    
class Game(models.Model):
    title = models.CharField(max_length= 20)
    cost = models.DecimalField(decimal_places=2, max_digits= 10)
    size = models.DecimalField(decimal_places=2, max_digits= 10)
    description = models.TextField()
    age_limited = models.BooleanField(default=True)
    buyer = models.ManyToManyField(Buyer)
