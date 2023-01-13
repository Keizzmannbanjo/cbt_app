import imp
from importlib import import_module
from typing import Final
from django.shortcuts import redirect, render, reverse, HttpResponse
from student.models import Student
from django.contrib.auth.decorators import login_required
import logging

from .models import Lecturer, Subject
from cbt.models import TestResult


logger = logging.getLogger('django')


@login_required
def dashboard(request):
    """     lecturer = Lecturer.objects.get(user=request.user)
        students = Subject.objects.get(title=lecturer.subject.title).students.all()
        subject = lecturer.subject
        test_results = TestResult.objects.filter(subject=subject)
        cascores = CAScore.objects.filter(subject=subject)
        exam_results = ExamResult.objects.filter(subject=subject)
        final_grades = FinalGrade.objects.filter(subject=subject)
        return render(request, 'lecturer/dashboard.html', {'lecturer': lecturer, 'students': students, 'subject': subject, 'test_results': test_results, 'cascores': cascores, 'exam_results': exam_results, 'final_grades': final_grades}) """
    lecturer = Lecturer.objects.get(user=request.user)
    subject_title = lecturer.subject.title
    students = Subject.objects.get(title=subject_title).students.all()
    test_results = TestResult.objects.filter(subject__title=subject_title)

    return render(request, 'lecturer/dashboard.html', {'students': students, 'lecturer': lecturer, 'test_results': test_results})
