from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.


def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        email_id = request.POST['email']
        password = request.POST['pwd']
        confirmpassword = request.POST['confpwd']

#     Check the signup requirements
        if len(username) > 20:
            messages.error(request, "Username must be under 20 characters")
            return redirect('home')

        if len(username) < 8:
            messages.error(request, 'Username must be atleast 8 characters')
            return redirect('home')

        if not username.isalnum():
            messages.error(request, "Username should only contain letters and numbers")
            return redirect('home')

        if len(password) > 40:
            messages.error(request, "Password must be under 40 characters")
            return redirect('home')

        if len(password) < 8:
            messages.error(request, 'Password must be atleast 8 characters')
            return redirect('home')

        symbols = ['!', '@', '#', '$', '&', '*']
        numbers = ['0','1','2','3','4','5','6','7','8','9']
        letters = list(password)

        if letters[0].isupper() is False:
            messages.error(request, "The First Letter of the password must be a capital letter")
            return redirect('home')


        sym = list(set(symbols).intersection(letters))
        num = list(set(numbers).intersection(letters))

        if sym == None:
            messages.error(request, "Password must contain alteast one of the following symbols: '!', '@', '#', '$', '&', '*'")
            return redirect('home')

        if num == None:
            messages.error(request,"Password must contain alteast one number")
            return redirect('home')

        if password != confirmpassword:
            messages.error(request, "The 2 passwords must be same")
            return redirect('home')

        myuser = User.objects.create_user(username, email_id, password)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.save()
        messages.success(request, "Your account has been successfully created")
        return redirect('home')

    else:
        return HttpResponse('404 - Not Found')


def login_(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        password = request.POST['pwd']

        user = authenticate(username=user_id, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials, Please try again")
            return redirect('home')

    else:
        return HttpResponse('404 - Not Found')

def logout_(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('home')