from django.contrib import admin
from .models import Staff, Guardian, StudentGroup, Student, GuardianStudent

admin.site.register(Staff)
admin.site.register(Guardian)
admin.site.register(StudentGroup)
admin.site.register(Student)
admin.site.register(GuardianStudent)