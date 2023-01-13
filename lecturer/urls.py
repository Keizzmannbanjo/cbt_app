from django.urls import path
from .views import *


app_name = 'lecturer'

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('create_quiz/', create_quiz, name="create_quiz"),
]
