from django.urls import path, include
from .views import *

urlpatterns = [
    path('notice',CollegeNotice.as_view(),name='notice')
] 

