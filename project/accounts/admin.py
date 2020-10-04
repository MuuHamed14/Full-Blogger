from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Profile
from import_export.admin import ImportExportModelAdmin

# admin.site.register(Profile)
@admin.register(Profile)
class ProfileImportExport(ImportExportModelAdmin):
    pass

