import re
from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,DeleteView,UpdateView
from main_page.views import MainPage
# from ProgressTracker import login_signup
from login_signup.forms import UserInfoForm
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
# Create your views here.

class LoginView(TemplateView):
    template_name = 'login_signup/login.html'
    
class SignupView(TemplateView):
    template_name = 'login_signup/signup.html'
    
def register(request):
    
    failed = False
    
    if(request.method == "POST"):
        
        userInfo = UserInfoForm(data = request.POST)
        
        if(userInfo.is_valid()):
            
            user = userInfo.save()
            user.set_password(user.password)
            user.save()
            print('done')
            
        else:
            failed = True
    else:
        userInfo = UserInfoForm()
        print('else')
        
    return render(request,'login_signup/signup.html',{'failed': failed,'userInfo':userInfo})
        
            
            
def user_login(request):
    failed = False
    
    if(request.method == "POST"):
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username,password)
        
        user = authenticate(username = username,password = password)
        
        print(type(user))
        if(user):
            if(user.is_active):
                login(request,user)
                # return HttpResponse("Logged")
                return HttpResponseRedirect(reverse( 'main_page:Main' ,kwargs={'username':user.username}))                
            else:
                return HttpResponse("Not logged")
        else:
            failed = True
            return render(request,'login_signup/login.html',{'failed':failed})
            
    else:
        return render(request,'login_signup/login.html',{'failed':failed})