from django.db import models
from lecturer.models import Subject
from student.models import Student



# Create your models here.
class Subject_Test(models.Model):
    subject = models.OneToOneField(Subject)


class Question(models.Model):
    text =models.CharField(max_length=500)
    subject =models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='test_questions')

class Choice(models.Model):
    text=models.CharField(max_length=300)
    is_correct = models.BooleanField(default=False)
    question=models.ForeignKey(Question,on_delete=models.CASCADE, related_name='question_choices')

class Test_Result(models.Model):
    subject = models.CharField(max_length=300)
    score = models.IntegerField()
    student = models.OneToOneField(Student, on_delete=models.CASCADE)

class CA_Result(models.Model):
    subject=models.CharField(max_length=300)
    score=models.IntegerField()
    student=models.OneToOneField(Student, on_delete=models.CASCADE)

class ExamResult(models.Model):
    subject = models.CharField(max_length=300)
    score = models.IntegerField()
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
