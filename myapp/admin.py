from django.contrib import admin
from . models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('task','is_completed','updated_at')  #list_display is default funtion in django for showing data in admin panel
    search_fields = ('task',)
admin.site.register(Task,TaskAdmin)