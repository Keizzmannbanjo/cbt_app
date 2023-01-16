from django.shortcuts import render, redirect, reverse, HttpResponse
from .models import Quiz, Question, Option, Answer, TestResult
from student.models import Student
from lecturer.models import Subject
from django.contrib.auth.decorators import login_required
import logging


# logger = logging.getLogger('django')


@login_required
def takeTest(request, subject_name):
    student = Student.objects.get(user=request.user)
    subject = Subject.objects.get(title=subject_name)
    quiz = None
    if student.quiz_results.all().count() > 0:
        for quiz_result in student.quiz_results.all():
            if quiz_result.subject == subject:
                return redirect(reverse("student:dashboard"))
            else:
                quiz = Quiz.objects.get(subject=subject)
                questions = quiz.question_set.all()
                return render(request, 'cbt/take_test.html', {'quiz': quiz, 'questions': questions})
    else:
        quiz = Quiz.objects.get(subject=subject)
        questions = quiz.question_set.all()
        return render(request, 'cbt/take_test.html', {'quiz': quiz, 'questions': questions})

    if request.method == 'POST':
        data = request.POST
        correct_answer_count = 0
        for x, y in data.items():
            if x == "csrfmiddlewaretoken":
                continue
            elif x == "quiz_title":
                quiz = Quiz.objects.get(id=int(y))
                print("quiz exist")
            else:
                print(int(y))
                option = Option.objects.get(id=int(y))
                question = Question.objects.get(id=int(x))
                answer = Answer(question=question,
                                option=option, answered_by=student)
                answer.save()
                if answer.option.is_correct == True:
                    correct_answer_count += 1
        test_result = TestResult(
            score=correct_answer_count, subject=quiz.subject, student=student)
        test_result.save()
        return redirect(reverse("student:dashboard"))

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
