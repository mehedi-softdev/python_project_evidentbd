from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from myapp.models import SortedArray
from django.http import JsonResponse
from datetime import datetime



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

@login_required
def logout_user(request):
    logout(request)
    return redirect('login')


# khoj the search part
@login_required
def khoj_the_search(request):
    if request.method == 'POST':
        inputs = request.POST['comma_separated_input']
        search_key = request.POST['search_key']
        search_key = int(search_key)
        keyPos = -1

        try: 
            input_list = inputs.split(',') if inputs else []
            integer_array = [int(value) for value in input_list]
            # sorting with buildin function
            integer_array = sorted(integer_array)
        
            # now applying binary search
            low = 0
            high = len(integer_array) - 1
            
        
            while(low <= high):
                mid = int((low + high) / 2)

                if integer_array[mid] == search_key:
                    keyPos = mid
                    break

                if integer_array[mid] > search_key:
                    high = mid - 1 
                else:
                    low = mid + 1  # Update low to search the right half
            
            if keyPos >= 0:
                messages.success(request, "True")
                # if success then store the sorted data to database
                user_id = request.user.id
                _timestamp = datetime.now()
                sorted_integer_array = sorted(integer_array, reverse=True) 
                _input_values_str = ', '.join(str(value) for value in sorted_integer_array)
                sorted_array = SortedArray.objects.create(
                    user_id = user_id,
                    input_values=_input_values_str,
                    timestamp= _timestamp
                )

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



# now implement api response function
@login_required
def get_all_input_values(request):

    if request.method == 'GET':
        start_datetime = request.GET.get('start_datetime', '')
        end_datetime = request.GET.get('end_datetime', '')
        user_id = request.GET.get('user_id', '')

        try:
            start_datetime = datetime.strptime(start_datetime, "%Y-%m-%d %H:%M:%S")
            end_datetime = datetime.strptime(end_datetime, "%Y-%m-%d %H:%M:%S")
        except Exception:
            # considered value error exception occured
            return JsonResponse({'status': 'error', 'message': 'Invalid date format.'}, status=400)
        
        input_values_queryset = SortedArray.objects.filter(
            user_id=user_id,
            timestamp__gte=start_datetime,
            timestamp__lte=end_datetime
        ).order_by('-timestamp')

        payload = []

        for input_value in input_values_queryset:
            payload.append({
                'timestamp': input_value.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                'input_values': input_value.input_values,
            })

        return JsonResponse({
            'status': 'success',
            'user_id': user_id,
            'payload': payload
        }, status=400)

    return JsonResponse({'status': 'error', 'message': 'Invalid request mthod'}, status=405)