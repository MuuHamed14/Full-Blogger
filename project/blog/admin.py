from django.contrib import admin
from .models import Post,Comment
from import_export.admin import ImportExportModelAdmin

# class PostAdmin(admin.ModelAdmin):
#     list_filter = ['post_date','post_update']
#     list_display = ['title','post_date','post_update']
#     search_fields = ['title','content']

# admin.site.register(Post,PostAdmin)
@admin.register(Post)
class PostImportExport(ImportExportModelAdmin):
    pass

# admin.site.register(Comment)  
@admin.register(Comment)
class CommentImportExport(ImportExportModelAdmin):
    pass

