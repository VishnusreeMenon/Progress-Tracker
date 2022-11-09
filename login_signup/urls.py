from django.urls import path
from . import views
app_name = 'login_signup'

urlpatterns = [
    path('',views.user_login,name = "Login"),
    path('register/',views.register,name="Signup"),
]