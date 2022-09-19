from django.db import models
from human_resource.models import *
from authenticate_user.models import User
# Create your models here.

class ApplyForJob(models.Model):
    resume = models.FileField(upload_to='user/resume/')
    job = models.ManyToManyField(Job,related_name='jobs')
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True,related_query_name='user_jobs')
    date = models.DateField(null=True,blank=True)
    interview_start_time = models.TimeField(null=True,blank=True)
    interview_end_time = models.TimeField(null=True,blank=True)
    
    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Job Application'
    
    

    
class StudentQualification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_qulification')
    course_name = models.CharField(max_length=150)
    grades = models.FloatField()
    session = models.CharField(max_length=150)
    institute = models.CharField(max_length=150)
    university_name = models.CharField(max_length=150)

    def __str__(self):
        return self.user.username

