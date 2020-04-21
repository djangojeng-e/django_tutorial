from django.contrib import admin

# Register your models here.

from .models import Student, Enrolment, Course


admin.site.register(Student)
admin.site.register(Enrolment)


class EnrolmentAdmin(admin.ModelAdmin):
    # list_display = ['student', 'course', 'enrolled_date', 'finished_date', 'academic_record']
    pass


admin.site.register(Course, EnrolmentAdmin)