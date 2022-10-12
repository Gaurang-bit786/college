from django.shortcuts import render, redirect
from django.views import View
from .models import ApplyForJob
from authenticate_user.models import *
from human_resource.models import *
from django.db.models import Q
from authenticate_user.models import *


class UserResume(View):

    def get(self,request,id):
        Resume.objects.get(id=id).delete()
        return redirect('profile')

    def post(self,request):
        resume = request.FILES.get('resume')
        Resume.objects.create(
            user=request.user,
            resume=resume
        )
        return redirect('profile')



class AllJobs(View):

    template_name = "all_jobs.html"
    
    def get(self,request):
        grade = request.user.user_qulification.filter(course_type='GRADUATE').first().grades
        all_jobs = ApplyForJob.objects.exclude(user=request.user).filter(job__requred_grades__lte=grade)
        print(all_jobs)
        context = {
            'jobs':all_jobs
        }
        return render(request,self.template_name,context)

class StudentJob(View):

    template_name = 'student_job.html'

    def get(self,request):
        return render(request,self.template_name)


class ApplyJob(View):  

    def get(self,request,id):
        apply = ApplyForJob.objects.get(id=id)
        apply.user.add(request.user)
        return redirect('all_jobs')


class Chat(View):

    template_name = 'chat.html'

    def get(self,request):
        user = User.objects.exclude(id=request.user.id)
        context = {
            'user':user
        }
        return render(request,self.template_name,context)

class ChatUser(View):

    template_name = 'chat.html'

    def get(self,request,id):
        get_user = User.objects.get(id=id)
        user = User.objects.exclude(id=request.user.id)

        context = {
            'get_user':get_user,
            'user':user
        }
        return render(request,self.template_name,context)

