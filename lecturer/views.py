from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
import logging

from .models import Lecturer, Subject
from cbt.models import TestResult, Quiz, Question, Option
from cbt.forms import QuizCreationForm


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


@login_required
def create_quiz(request):
    form = QuizCreationForm()
    if request.method == 'POST':
        form = QuizCreationForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            lecturer = Lecturer.objects.get(user=request.user)
            quiz.subject = lecturer.subject
            quiz.save()
            return redirect(reverse('lecturer:dashboard'))
    return render(request, 'lecturer/create_quizz.html', {'form': form})


@login_required
def add_question(request):
    if request.method == "POST":
        data = request.POST
        lecturer = Lecturer.objects.get(user=request.user)
        subject = Subject.objects.get(title=lecturer.subject.title)
        quiz = Quiz.objects.get(subject=subject)
        print(data)
        option_count = 1
        correct_option_no = 0
        question = None
        for x, y in data.items():
            if x == "csrfmiddlewaretoken":
                continue
            elif x == "question_text":
                question = Question(quiz=quiz, text=y)
                question.save()
            elif x == "correct_option_no":
                correct_option_no = int(y)
            else:
                option = Option(question=question, text=y, order=option_count)
                if correct_option_no == option_count:
                    option.is_correct = True
                option.save()
                option_count += 1
        return redirect(reverse("lecturer:dashboard"))
    return render(request, "lecturer/set_questions.html")


@login_required
def view_exam(request):
    quiz = None
    questions = None
    lecturer = Lecturer.objects.get(user=request.user)
    subject = lecturer.subject
    try:
        quiz = Quiz.objects.get(subject=subject)
        questions = Question.objects.filter(quiz=quiz)
    except:
        pass
    return render(request, 'lecturer/view_exam.html', {'quiz': quiz, 'questions': questions})
