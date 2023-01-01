from django.db import models
from lecturer.models import Subject
from student.models import Student

class Question(models.Model):
    text =models.CharField(max_length=500)
    subject =models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='questions') # ? related name to access all questions from subject object
    option_a = models.CharField(max_length=200)
    option_b = models.CharField(max_length=200)
    option_c = models.CharField(max_length=200)
    option_d = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    

class TestResult(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='test_results') # ? related name to access all test results from subject object
    score = models.IntegerField(default=0)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='test_results') # ? related name to access all test results from student object

    

class CAScore(models.Model):
    subject=models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subject_ca_results') # ? related name to access all ca results from subject object
    test_score = models.IntegerField(default = 0)
    other_score = models.IntegerField(default = 0)
    score=models.IntegerField(default=0)
    student=models.ForeignKey(Student, on_delete=models.CASCADE, related_name='ca_scores') # ? related name to access all ca results from student object

class ExamResult(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subject_exam_results') # ? related name to access all exam results from subject object
    score = models.IntegerField(default=0)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='exam_results') # ? related name to access all exam results from student object

class FinalGrade(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subject_final_results') # ? related name to access all test results from subject object
    ca_score = models.IntegerField(default=0)
    exam_score = models.IntegerField(default = 0)
    grade = models.CharField(max_length=2, default='-'
        )
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='final_grades', null=True) # ? related name to access all final grades from student object