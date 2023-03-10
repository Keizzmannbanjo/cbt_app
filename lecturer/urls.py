from django.urls import path
from .views import *


app_name = 'lecturer'

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('create_quiz/', create_quiz, name="create_quiz"),
    path('add_question/<int:pk>/', add_question, name="add_question"),
    path('view_exam/<int:pk>/', view_exam, name="view_exam"),
    path('view_quizzes/<str:subject_name>/', view_quzzes, name="view_quizzes"),
    path('add_students_to_quiz/<int:pk>/', add_students_to_quiz,
         name="add_students_to_quiz"),
         path('remove_student_from_quiz/<int:quizlist_id>/<int:student_id>/',remove_from_quiz, name="remove_from_quiz"),
]
