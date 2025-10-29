from django.contrib import admin
from .models import student,teacher,leave
# Register your models here.
admin.site.register(student)
admin.site.register(teacher)
admin.site.register(leave)

admin.site.site_header = "Leave Management System Admin"