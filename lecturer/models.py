from django.db import models
from accounts.models import User

# Create your models here.


class Subject(models.Model):
    title = models.CharField(max_length=300)
    code = models.CharField(max_length=7)

    def __str__(self):
        return self.title


class Lecturer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    surname = models.CharField(max_length=25)
    email = models.EmailField()
    first_name = models.CharField(max_length=25)
    other_name = models.CharField(max_length=25)
    subject = models.OneToOneField(Subject, related_name='lecturer', null=True, on_delete=models.SET_NULL) # ? related name to access lecturer from subject object

    def __str__(self):
        return f"{self.surname} {self.first_name}"
