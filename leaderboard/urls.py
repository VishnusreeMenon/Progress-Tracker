from django.contrib import admin
from django.urls import path,include
from leaderboard import views

app_name  = "leaderboard"

urlpatterns = [
    path('',views.get_key, name = "Leaderboard"),
]