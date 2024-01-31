
from django.urls import path
from . import views as vw
from .views import Show_Task
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',vw.SignUpPage, name='signup'),
    path('show-task/',login_required(Show_Task), name='home'),
    path('sign-up/',vw.SignUpPage, name='signup'),
    path('login/',vw.loginPage, name='login'),
    path('logout/',vw.logoutPage, name='logout'),
]
