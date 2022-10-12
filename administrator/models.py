from django.db import models
from authenticate_user.models import Course
# Create your models here.



class Notice(models.Model):
    title = models.CharField(max_length = 150)
    description = models.CharField(max_length = 150)
    date = models.DateField(auto_now_add=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,null=True,blank=True)
    file = models.FileField(upload_to='notice/',null=True,blank=True)
    def __str__(self):
        return self.title


class Teacher(models.Model):
    image = models.ImageField(upload_to='teacher/')
    name = models.CharField(max_length=150)
    facebook = models.URLField(max_length=250)
    gmail = models.URLField(max_length=250)
    twitter = models.URLField(max_length=250)
    linkedin = models.URLField(max_length=250)

    def __str__(self):
        return self.name