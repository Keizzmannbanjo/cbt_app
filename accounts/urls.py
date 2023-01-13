from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('', generalSignIn, name='signin'),
    path('create_student/', createStudent, name='create_student'),
    path('create_lecturer/', createLecturer, name='create_lecturer'),
    path('registrar/', registrarSignIn, name='registrar_signin'),
    path('registrar/dashboard/', registrarDashboard, name='registrar_dashboard'),
    path('create_subject/', createSubject, name="create_subject"),
    # path('student/signout/', studentSignOut, name = 'student_signout'),
    # path('student/register/', studentRegister, name = 'register_student'),
]
