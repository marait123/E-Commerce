from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpRequest
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from . import forms
def test(request):
    return JsonResponse({'soso':1,'hi':'lol'},status=204)

def home(request):
    form = forms.LoginForm()
    context = {
        'form':form
    }
    return render(request, 'home.html',context=context)

def login(request):
    form = forms.LoginForm(request.POST or None)
    context = {
        'form': form
    }
    if request.method.lower() == "get":
        return render(request, 'auth/signin.html',context=context) 
    if form.is_valid():
        data = form.cleaned_data
        user = authenticate(request, **data)
        if user is not None:
            auth_login(request,user)
        else:
            context['error'] = 'invalid username or password'
    else:
        context['error'] = 'invalid form passed'
    return redirect('/home')
def register(request:HttpRequest):
    form = forms.RegisterForm()
    myContext = {'form':form}
    return render(request, 'auth/register.html',context=myContext)
def signup(request:HttpRequest):
    if request.method.lower() == "post":
        form = forms.RegisterForm(request.POST or None)
        if form.is_valid():
            data = form.cleaned_data                 
            print(data)
            del data['password2']
            try:
                user = User.objects.create(**data)
                print(user)
            except:
                return redirect('/register')
        else:
            print("invalid username or unmatched password")
            myContext = {'form':form}
            return render(request, 'auth/register.html',context=myContext)
        myContext = {'form':form}
        return redirect('/home')
    else:
        context['error'] = "this method isn't supported"
        return render(request, 'home.html',context=myContext)

def logoutUser(request:HttpRequest):
    context = {}
    if request.user.is_authenticated:
        logout(request)
    return redirect('/home')

def contact(request:HttpRequest):
    form = forms.ContactForm(request.POST or None)
    context = {
        'form':form
    }
    if(request.method.lower()=="post"):
        print(request.POST)
    return render(request, 'home.html',context=context)