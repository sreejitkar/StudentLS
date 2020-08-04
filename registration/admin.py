from django.contrib import admin
from .models import *
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('s_id', 's_name', 's_class', 's_sex')
    list_display_links = ('s_name', 's_class')
    list_per_page = 25

admin.site.register(Student,StudentAdmin)
admin.site.register(Classroom)
admin.site.register(Subjects)
admin.site.register(SubToClassMap)
admin.site.register(SubtoStudentMap)
