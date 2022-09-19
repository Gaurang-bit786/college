from django.urls import path, include
from .views import *


urlpatterns = [
    path('login',LoginUser.as_view(),name='login'),
    path('',Home.as_view(),name='home'),
    path('logout',logout_user,name='logout_user'),
    path('contact',Contact.as_view(),name='contact'),
    path('register',Register.as_view(),name='register'),
]
