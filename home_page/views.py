from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,DeleteView,UpdateView
# Create your views here.

class IndeXView(TemplateView):
    template_name = "home_page/landing_page.html"
    