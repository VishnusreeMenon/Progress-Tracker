from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,DeleteView,UpdateView,FormView
from .forms import FilterForm
from my_progress.models import Exercise
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
# Create your views here.
class Leaderboard(ListView):
    
    model = Exercise
    context_object_name = "exercises"
    template_name = "leaderboard/leaderboard.html"


def get_key(request):
    form = FilterForm()
    if request.method == "POST":
        form = FilterForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect(reverse( 'Leaderboard:leaderboard' ,kwargs={'filter_by':form.filter_by}))
        
            
    return render(request,"leaderboard/leaderboard.html",{"form":form})