from curses import def_shell_mode
from email import message
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from httplib2 import Authentication
from .forms import DemoUserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import authenticate


# Create your views here.
def index(request):
    return render(request,"demoapp/index.html")

def register(request):
    form = DemoUserForm(request.POST, request.FILES)
    
    if form.is_valid():
        role = form.cleaned_data['role']
        pass1 = form.cleaned_data['pass1']
        pass2 = form.cleaned_data['pass2']
        if pass1 != pass2:
            return HttpResponse("sorry password doesnt match")
        elif role =='Doctor':
            form.save()
            return render(request,"demoapp/sample.html")
        elif role =='Patient':
            form.save()
            return render(request,"demoapp/index.html")
        else:
            return render(request,"demoapp/index.html")


    return render(request,"demoapp/register.html",{
        "form":form
    })

def sample(request):
    return render(request,"demoapp/sample.html")
