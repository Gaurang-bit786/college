from django.contrib import admin
from .models import *
from import_export.admin import ImportExportMixin
# Register your models here.



@admin.register(ApplyForJob)
class ApplyForJobAdmin(ImportExportMixin,admin.ModelAdmin):
    pass


