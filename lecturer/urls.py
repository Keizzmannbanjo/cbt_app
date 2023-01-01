from django.urls import path 
from .views import *


app_name = 'lecturer'

urlpatterns = [ 
    path('dashboard', dashboard, name ='dashboard'),
    path('student/find_student/',findStudent, name ='find_student'),
]