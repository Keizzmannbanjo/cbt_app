from django.shortcuts import render, redirect, HttpResponse
from .models import CAScore, Question, TestResult, FinalGrade
from student.models import Student
from lecturer.models import Subject
from django.contrib.auth.decorators import login_required
import logging 

# logger = logging.getLogger('django')


@login_required
def takeTest(request, subject_name):
    """ subject = subject_name
    try:
        test_result = Subject.objects.get(title = subject_name).test_results.get(student__user = request.user)
        if test_result:
            return redirect('student:dashboard')
    except:
        pass
    questions = Question.objects.filter(subject__title = subject_name).order_by('id')
    questions_count = questions.count()
    return render(request, 'cbt/test.html',context = {'questions': questions, 'subject' : subject, 'questions_count': questions_count}) """
    return HttpResponse("Test to take")

@login_required
def handleTestSubmit(request):
    """ score = 0
    if request.method == 'POST':
        data = request.POST
        questions = Question.objects.filter(subject__title = data['subject_title']).order_by('id')
        for q in questions:
            if q.text  in data.keys():
                choice = data[q.text]
                if choice == q.answer:
                    score += 1
        test_result = TestResult.objects.create(
            subject = Subject.objects.get(title = data['subject_title']),
            score = score,
            student = Student.objects.get(user = request.user)
        )
        test_result.save()
        return redirect('student:dashboard')
    return redirect('student:dashboard') """
    return HttpResponse("Test Submitted")

