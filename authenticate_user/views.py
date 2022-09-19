from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout, authenticate
from .models import *


class LoginUser(View):
    template_name = 'login.html'
    

    def get(self,request):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return render(request, self.template_name)
            
    def post(self,request):
        user = authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        
        if user:
            login(request,user)
            return redirect('home')
        else:
            context = {
                'details':'Invalid Cridential'
            }
            return render(request, self.template_name,context)





class Home(View):
    template_name = 'home.html'
    
    def get(self,request):
        return render(request,self.template_name)


class Contact(View):
    template_name = 'contact.html'

    def get(self,request):
        return render(request,self.template_name)

    def post(self,request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = ContactDetails.contact.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        print()
        return redirect('contact')


class Register(View):
    def post(self,request):
        print(request.POST)
        User.objects.create_users(
            username = request.POST.get('roll'),
            password = request.POST.get('password'),
            first_name = request.POST.get('first_name'),
            last_name = request.POST.get('last_name'),
            email = request.POST.get('email')
        )
        return redirect('home')


def logout_user(request):
    logout(request)
    return redirect('home')