from django.urls import path
from . import views

app_name = 'main_page'


urlpatterns = [
    path('<slug:username>/',views.MainPage.as_view(),name='Main'),
    path('logout',views.user_logout,name = 'Logout')
]