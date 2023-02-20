from django.shortcuts import render
from cbt.models import Subject, TestResult, QuizList
from .models import Student
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    student = Student.objects.get(user=request.user)
    students_quizzes = [quizlist.quiz for quizlist in QuizList.objects.all(
    ) if student in quizlist.candidates.all()]
    all_quizzes_count = len(students_quizzes)
    completed_quizzes_results = student.quiz_results.all()
    completed_quizzes = []
    if len(completed_quizzes_results) > 0:
        completed_quizzes = [
            result.quiz for result in completed_quizzes_results]
    completed_quizzes_count = len(completed_quizzes)
    uncompleted_quizzes = []
    if completed_quizzes_count < len(students_quizzes):
        uncompleted_quizzes = [
            quiz for quiz in students_quizzes if quiz not in completed_quizzes]
    uncompleted_quizzes_count = all_quizzes_count - completed_quizzes_count
    context = {"student": student, 'student_quizzes': students_quizzes, 'all_quizzes_count': all_quizzes_count,
               'completed_quizzes': completed_quizzes, 'completed_quizzes_count': completed_quizzes_count, 'uncompleted_quizzes': uncompleted_quizzes, 'uncompleted_quizzes_count':uncompleted_quizzes_count}
    return render(request, 'student/dashboard.html', context)


@login_required
def viewSubjects(request):
    student = Student.objects.get(user=request.user)
    subjects = student.subjects
    return render(request, 'student/subjects.html', context={'subjects': subjects})
