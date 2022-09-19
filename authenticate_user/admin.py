from django.contrib import admin
from .models import *
from student.models import *
# Register your models here.



class UserQualification(admin.TabularInline):
    model = StudentQualification
    extra = 0


class UserAdmin(admin.ModelAdmin):
    inlines = [UserQualification]
    list_display = ['username','email','phone_number','is_superuser','is_staff','is_active']
    list_filter = ['username','email','phone_number','is_superuser','is_staff','is_active']
    search_fields = ['username','email','phone_number','is_superuser','is_staff','is_active']
    list_editable = ['is_staff','is_active']
    list_max_show_all = 10
    list_per_page = 20

    fields = (
        ('profile_pic','username','first_name','last_name','email','is_active','is_staff','is_superuser','date_joined','address','groups','user_permissions')
    )

admin.site.register(User,UserAdmin)



admin.site.register(Addres)
admin.site.register(ContactDetails)
admin.site.register(Subscriber)