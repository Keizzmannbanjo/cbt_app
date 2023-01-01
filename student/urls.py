from django.urls import path
from .views import *

app_name = 'student'

urlpatterns = [
    path('dashboard/',dashboard, name ='dashboard' ),
    path('view_subjects/', viewSubjects, name = 'view_subjects'),
    # path('<str:subject_name>/view_grade/',viewSubjectGrade, name ='view_subject_grade'),
    # path('/subject/<str:subject_name>/view_grade/', viewSubjectGrade, name ='view_subject_grade')
]