from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import CustomUser
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate



def home(request):
    return render(request, "myapp/khoj_the_search.html")

def registration(request):
    if request.method == "POST":

        _fullname = request.POST["fullname"]
        _email = request.POST['email']
        _password = request.POST['password']
        

        try: 
            # email validation (i.e if already exists or not)
            existing_user = CustomUser.objects.get(email=_email)
            messages.error(request, "User already registered!")
        except CustomUser.DoesNotExist:
            # now store user to database
            user = CustomUser(fullname=_fullname, 
                              email=_email, 
                              password=make_password(_password))
            user.save()
            messages.success(request, 'User registered successfully!')
        
    
    return render(request, "myapp/registration.html")


def login(request): 

    if request.method == 'POST':
        _email = request.POST['email']
        _password = request.POST['password']
        
        try:
            user = CustomUser.objects.get(email=_email)
            if check_password(_password, user.password):
                # then login success
                return redirect('/')
            else:
                messages.error(request, "Invalid credentials!")
        except CustomUser.DoesNotExist:
            messages.error(request, "Invalid credentials!")


    return render(request, "myapp/login.html")