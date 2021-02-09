from django.contrib import admin
from .models import Teacher, Question # importing the teacher model into the admin


admin.site.register(Teacher)
admin.site.register(Question)
# Register your models here.
