from django.shortcuts import render
from .models import Student
from django.contrib.auth.decorators import login_required




@login_required
def dashboard(request):
    student = Student.objects.get(user = request.user)
    # test_results = TestResult.objects.filter(subject = subject)
    # cascores = CAScore.objects.filter(subject = subject)
    # exam_results = ExamResult.objects.filter(subject = subject)
    # final_grades = FinalGrade.objects.filter(subject = subject)
    context = {"student" : student}
    return render(request, 'student/dashboard.html', context)


@login_required
def viewSubjects(request):
    student = Student.objects.get(user = request.user)
    subjects = student.subjects
    return render(request, 'student/subjects.html',context =  {'subjects': subjects})






