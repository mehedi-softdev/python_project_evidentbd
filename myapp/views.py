from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


#defualt path (/accounts/login/)
@login_required(redirect_field_name="")
def home(request):
    return render(request, "myapp/khoj_the_search.html")

def registration(request):
    if request.method == "POST":

        _firstname = request.POST["firstname"]
        _lastname = request.POST['lastname']
        _email = request.POST['email']
        _password = request.POST['password']
        
        # for now considering saving error causes for username intigrity problem
        try:
            user = User(first_name=_firstname, last_name=_lastname, email=_email)
            user.username = _email
            user.set_password(_password)
            user.save()
            messages.success(request, 'User registered successfully!')
            return redirect('login')
        except Exception:
            messages.error(request, "User already registered")
       
            
    return render(request, "myapp/registration.html")


def login_user(request): 

    if request.method == 'POST':
        _email = request.POST['email']
        _password = request.POST['password']
        

        user = authenticate(request, username=_email, password=_password)
    
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials!")

    return render(request, "myapp/login.html")


def logout_user(request):
    logout(request)
    return redirect('login')


# khoj the search part
def khoj_the_search(request):
    if request.method == 'POST':
        inputs = request.POST['comma_separated_input']
        search_key = request.POST['search_key']
        search_key = int(search_key)

        try: 
            input_list = inputs.split(',') if inputs else []
            integer_array = [int(value) for value in input_list]
            # sorting with buildin function
            integer_array = sorted(integer_array)
            # now applying binary search
            low = 0
            high = len(integer_array) - 1
            keyPos = -1
        
            while(low <= high):
                mid = int((low + high) / 2)
                if integer_array[mid] > search_key:
                    high -= 1
                elif integer_array[mid] < search_key:
                    low += 1
                else:
                    keyPos = mid
                    break
        
            if keyPos >= 0:
                messages.success(request, "True")
            else:
                messages.error(request, "False")

        except Exception:
            pass

        
        data = {
            'array': inputs,
            'search_key': search_key,
        }
        return render(request, "myapp/khoj_the_search.html", {'data': data})
       
    else:
        return redirect("home")