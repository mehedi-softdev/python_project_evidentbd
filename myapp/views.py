from django.shortcuts import render


def registration(request):
    return render(request, "myapp/registration.html")


def login(request): 
    return render(request, "myapp/login.html")