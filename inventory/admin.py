from django.contrib import admin
from .models import *
# Register your models here.
from import_export.admin import *
@admin.register(mobile)
class ViewAdmin(ImportExportModelAdmin):
    pass