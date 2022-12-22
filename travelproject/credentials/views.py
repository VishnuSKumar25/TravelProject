from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(req):
    if req.method == 'POST':
        username = req.POST['username']
        first_name = req.POST['first_name']
        last_name = req.POST['last_name']
        email = req.POST['email']
        password = req.POST['password']
        cnfpassword = req.POST['cnfpassword']
        if password == cnfpassword:
            if User.objects.filter(username=username).exists():
                messages.info(req, "Username already exists. Try another one")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(req, "Email id already exists. Try another one")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)

                user.save()
                print("User Created Successfully")
        else:
            messages.info(req, "Password not matched")
            return redirect('register')
        return redirect('login')

    return render(req, "register.html")

def login(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(req, user)
            return redirect('/')

        else:
            messages.info(req, "Invalid Credentials. Retry")
            return redirect('login')

    return render(req, "login.html")

def logout(req):
    auth.logout(req)
    return redirect('/')