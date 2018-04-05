from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Class)
admin.site.register(Student)
admin.site.register(Subjects)
admin.site.register(SubjectEnroll)
admin.site.register(Parents)
admin.site.register(Section)