from imaplib import _Authenticator
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def SignUpPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1==pass2 :
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
        else:
            #messages.add_message(request, messages., f'Password doesnot match')
            return HttpResponse("Password doesnt match")    #HttpResponseRedirect(request.path)
        #print(uname,email,pass1,pass2)
        return render(request,'login.html')

    return  render(request,'signup.html')


def loginPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(username=uname,password=pass1)
        if user is not None:
            login(request,user)
            return render(request,'index.html')
        else:
            return HttpResponse("Invalid Username or Password")
    return  render(request,'login.html')

@login_required
def logoutPage(request):
    logout(request)
    return render(request,'index.html')

@login_required
def Show_Task(request):
    pass