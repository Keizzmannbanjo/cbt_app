import imp
from django.db import models
from cbt.models import Subject

# Create your models here.


class Subject(models.Model):
    title = models.CharField(max_length=300)


class Lecturer(models.Model):
    subject = models.OneToOneField(Subject, related_name='subject_lecturer')