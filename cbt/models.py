from django.db import models
from lecturer.models import Subject
from student.models import Student


class Quiz(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name="quizzes", null=False)


class QuizList(models.Model):
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name="quiz_canditates", null=False)
    candidates = models.ManyToManyField(Student)


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)


class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    order = models.IntegerField(default=0)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answered_by = models.ForeignKey(Student, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)


class TestResult(models.Model):
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name='quiz_results')
    score = models.IntegerField(default=0)
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name='quiz_results')
