from django.contrib import admin
from .models import StudentProfile, Subject, Marks

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'roll_no', 'department', 'year', 'semester']
    search_fields = ['roll_no', 'user__username']

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'credits', 'semester']

@admin.register(Marks)
class MarksAdmin(admin.ModelAdmin):
    list_display = ['student', 'subject', 'internal_marks', 'external_marks', 'total_marks', 'grade']