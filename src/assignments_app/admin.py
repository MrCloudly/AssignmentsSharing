from django.contrib import admin
from .models import *

# Register your models here.
class AssignmentAdmin(admin.ModelAdmin):
    list_display=("id","label", "description", "time_cost", "priority")

class StatusAdmin(admin.ModelAdmin):
    list_display=("id","status_type","occurrence_time")

class DeveloperAdmin(admin.ModelAdmin):
    list_display=("id", "first_name", "last_name", "pseudonym")

class IssueAdmin(admin.ModelAdmin):
    list_display=("id", "label", "description")


admin.site.register(Assignment,AssignmentAdmin)
admin.site.register(Status,StatusAdmin)
admin.site.register(Developer,DeveloperAdmin)
admin.site.register(Issue,IssueAdmin)