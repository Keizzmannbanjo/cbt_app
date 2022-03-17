from django.db import models
from lecturer.models import Subject

# Create your models here.

class Student(models.Model):
    subjects =models.ManyToManyField(Subject, related_name='subject_students')