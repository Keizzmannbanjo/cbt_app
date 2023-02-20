from django.urls import path 
from .views import * 

app_name = 'cbt'

urlpatterns = [ 
    path('take_quiz/<int:pk>/', take_quiz, name = 'take_quiz'),
]