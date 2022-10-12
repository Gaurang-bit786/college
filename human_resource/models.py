from django.db import models
from authenticate_user.models import User
from django.template.defaultfilters import slugify
from django.db import transaction
from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.



class Job(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length = 150,null=True,blank=True)
    course = models.CharField(max_length=150)
    requred_grades = models.CharField(max_length=150)
    company_name = models.CharField(max_length=150)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Available Job'
    
 
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Job,self).save(*args,**kwargs)


    def __str__(self):
        return self.title



class SendMail(models.Model):
    title = models.CharField(max_length = 150)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    
    description = RichTextUploadingField(blank=True)
    

    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        super(SendMail,self).save(*args,**kwargs)


@receiver(post_save, sender=SendMail)
def send_mail_to_subs(sender, instance, created, **kwargs):
    lt = []
    lt.append(instance.user.email)
    send_mail(instance.title,instance.description,settings.EMAIL_HOST_USER,lt)