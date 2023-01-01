from django.urls import path 
from .views import * 

app_name = 'cbt'

urlpatterns = [ 
    path('take_test/<str:subject_name>/', takeTest, name = 'take_test'),
    path('submit_test/', handleTestSubmit, name ="submit_test"),
]