from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import *
# Register your models here.


@admin.register(Notice)
class NoticeAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ['title','description','date','course']



@admin.register(Teacher)
class TecherAdmin(ImportExportMixin,admin.ModelAdmin):
    pass

