from django.contrib import admin
from .models import *
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
# Register your models here.
from import_export.admin import *
@admin.register(phone)

class ViewAdmin(ImportExportModelAdmin):
    pass

admin.site.site_header = 'vPhrase Admin Panel '
site_title = ugettext_lazy('vPhrase Admin Panel ')
index_title = ugettext_lazy('vPhrase Admin Panel ')