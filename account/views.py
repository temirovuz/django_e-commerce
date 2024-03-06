from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

from account.models import User


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 != password2:
            return HttpResponse('Passwords do not match')
        else:
            phone = request.POST['phone']
            my_user = User.objects.create_user(username=username, email=email, password=password1, phone_numer=phone)
            my_user.save()
            
