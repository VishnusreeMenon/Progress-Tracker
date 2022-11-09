from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,DeleteView,UpdateView
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
# Create your views here.
class MainPage(TemplateView):
    
    template_name = 'main_page/main.html'

@login_required     
def user_logout(request):
    
    logout(request)
    return HttpResponseRedirect(reverse('Index'))