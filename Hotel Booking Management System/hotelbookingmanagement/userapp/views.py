from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Users  # Assuming Users is the model for additional user details
from adminapp.models import Hotel
from django.contrib.auth import authenticate, login as lg

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        gender = request.POST['gender']
        img = request.FILES.get('image')  # Use get() to avoid KeyError if 'image' is not in request.FILES
        mobile = request.POST['phone']

        if password1 != password2:
            messages.error(request, 'Passwords do not match')
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
            return redirect('signup')

        user = User.objects.create_user(username=username, password=password1, first_name=first_name,
                                         last_name=last_name, email=email)
        user.save()
        user_profile = Users.objects.create(user_id=user, gender=gender, img=img, mobile=mobile)
        user_profile.save()

        # Redirect to login page upon successful signup
        return redirect('login')

    return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if len(username) == 4:
                lg(request, user)
                messages.success(request, 'Login successful. Welcome!')
                return redirect('managementhomepage')
            else:
                lg(request, user)
                messages.success(request, 'Login successful. Welcome!')
                return redirect('userhomepage')
        else:
            messages.error(request, 'Invalid Credentials')
            return render(request, 'login.html', {'fail': True})
    else:
        return render(request, 'login.html', {'fail': False})

def logout(request):
    return render(request,'home.html')

def userhomepage(request):
    return render(request,'userhomepage.html')

def bookhotel(request):
    hotels = Hotel.objects.all()
    return render(request,'bookhotel.html',{'hotels': hotels})

def contactus(request):
    return render(request,'contactus.html')
