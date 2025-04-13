from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse

#for authentications
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate

#necessay imports of models and forms
from .models import User,Profile
from .forms import SignUpForm,ProfileForm

#for messages
from django.contrib import messages
# Create your views here.

def sign_up(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"your account has been successfully created")
            return HttpResponseRedirect(reverse('Login_App:login')) 
    
    return render(request,'Login_App/signup.html',context={'form':form})    

def login_user(request):
    form= AuthenticationForm()
    if request.method=='POST':
        form= AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password= form.cleaned_data.get('password')
            user= authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('Shop_App:home'))
    
    return render(request,'Login_App/login.html',context={'form':form})               


@login_required
def logout_user(requset):
    logout(requset)
    messages.warning(requset,"you are logged out")
    return HttpResponseRedirect(reverse('Shop_App:home'))
    
    
@login_required
def user_profile(request):
    profile= Profile.objects.get(user=request.user)
    form= ProfileForm(instance=profile)  
    
    if request.method=='POST':
        form= ProfileForm(request.POST,instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request,"profile updation succedd")
            form= ProfileForm(instance=profile)
    
    return render(request,'Login_App/change_profile.html',context={'form':form})          