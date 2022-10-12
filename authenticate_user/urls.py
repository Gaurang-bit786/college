from django.urls import path, include
from .views import *


urlpatterns = [
    path('login',LoginUser.as_view(),name='login_user'),
    path('',Home.as_view(),name='home'),
    path('logout',logout_user,name='logout_user'),
    path('contact',Contact.as_view(),name='contact'),
    path('register',Register.as_view(),name='register'),
    path('profile',Profile.as_view(),name='profile'),
    path('qualification',Qualification.as_view(),name='qualification'),
    path('qualification/<int:id>',Qualification.as_view(),name='qualification-del'),
    path('dashboard',Dashboard.as_view(),name='dashboard'),
]
