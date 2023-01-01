from django.contrib import admin
from .models import *

admin.site.register(Question)
admin.site.register(TestResult)
admin.site.register(CAScore)
admin.site.register(ExamResult)
admin.site.register(FinalGrade)
