from django.db import models
from django.template.defaultfilters import slugify

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
