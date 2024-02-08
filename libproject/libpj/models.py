from django.db import models
import uuid
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string

# Create your models here.
User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    year = models.IntegerField()
    name = models.CharField(max_length=40, default="None")
    surename = models.CharField(max_length=40, default="None")
    trust = models.IntegerField(blank=True, null=True)
    borrowed = models.IntegerField(blank=True, null=True)
    on_time = models.IntegerField(blank=True, null=True)
    ans = models.CharField(max_length=5250, default="None")

    api_key = get_random_string(length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    premium = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username

class Book(models.Model):
    Title = models.CharField(max_length=100, default="None")
    author = models.CharField(max_length=40, default="None")
    genre = models.CharField(max_length=40, default="None")
    id_book = models.IntegerField()
    year = models.IntegerField()
    description = models.CharField(max_length=400, default="None")
    age_rating = models.CharField(max_length=40, default="None")
    condition = models.CharField(max_length=90, default="None")
    borrowed = models.IntegerField(blank=True, null=True)
    pages = models.IntegerField(blank=True, null=True)
    img = models.ImageField(upload_to='img', default='')
    
    def __str__(self):
        return self.Title

class Pwdlist(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username