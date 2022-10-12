from django.contrib import admin
from .models import *
from import_export.admin import ImportExportMixin
# Register your models here.


@admin.register(Job)
class JobAdmin(ImportExportMixin,admin.ModelAdmin):
    pass


@admin.register(SendMail)
class SendMailAdmin(ImportExportMixin,admin.ModelAdmin):
    pass


