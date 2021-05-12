from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .forms import SignupForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here

def Home(request):

    return render(request, 'home.html') 

def Register(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Registration Successfully Done')
            form.save()
            return HttpResponseRedirect('/login')

    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form':form}) 

def Login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password) 
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Successfully login')
                    return HttpResponseRedirect('/')
                else:
                    form = LoginForm()
                    messages.success(request, 'Something went wrong')
                    return HttpResponseRedirect('/login')
        else:
            form = LoginForm()
        return render(request, 'login.html', {'form':form}) 
    else:
        messages.info(request, 'Already login')
        return HttpResponseRedirect('/')

def Logout(request):
    logout(request)
    messages.success(request, 'You need to be logged in to log out!')
    return HttpResponseRedirect('/')