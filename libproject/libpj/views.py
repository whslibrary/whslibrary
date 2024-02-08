from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from .models import Profile, Pwdlist, Book
import random
import time
from datetime import datetime
from django.http import JsonResponse
#from .serializers import Paper1serializer, Paper2serializer, Paper3serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import openai, os
from itertools import chain
import re

@login_required(login_url="signin")
def index(request): 
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    books = Book.objects.all()
    context = {
        'user':user_object,
        'data':user_profile,
        'book':books,
    }

    return render(request, 'home.html', context)
    
@login_required(login_url="signin")
def book_search(request):
    query = request.GET.get('q')
    if query:
        # Filter books with an exact case-insensitive match to the query
        books = Book.objects.filter(Title__iexact=query)
    else:
        books = Book.objects.all()
    return render(request, 'home.html', {'books': books, 'query': query})


@login_required(login_url="signin")
def book_showcase(request):
    books = Book.objects.all().order_by('Title')
    return render(request, 'home.html', {'book': books})

@login_required(login_url="signin")
def upload_(request):
    if request.method == 'POST':
        image = request.FILES.get('img')
        year = request.POST['year']
        pages = request.POST['pages']
        title = request.POST['title']
        id_book = request.POST['id_book']
        description = request.POST['description']
        age_rating = request.POST['age_rating']
        condition = request.POST['condition']
        author = request.POST['author']

        new_book = Book.objects.create(Title=title, id_book=id_book, author=author, year=year, description=description, age_rating=age_rating, condition=condition, pages=pages, img=image)

        new_book.save()

        return render(request, 'upload.html')
    else:
        pass

@login_required(login_url="signin")
def upload(request):
    return render(request, 'upload.html')

@login_required(login_url="signin")
def library(request):
    return render(request, 'library.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        year = request.POST['year']
        email = request.POST['email']
        name = request.POST['name']
        surename = request.POST['surename']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                new_pwdlist = Pwdlist.objects.create(username=username, email=email, password=password)
                new_pwdlist.save()

                #Log user + redirect to settings
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                #create profile for user

                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id, year=year, name=name, surename=surename)
                new_profile.save()
                return redirect('/')
        else:
            messages.info(request, 'Password Not Mathching')
            return redirect('signup')
    else:
        return render(request, 'signup.html')

def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('signin')
    else:
        return render(request, 'signin.html')


@login_required(login_url="signin")
def logout(request):
    auth.logout(request)
    return redirect('signin')
