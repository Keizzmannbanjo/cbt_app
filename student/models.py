from django.db import models


from lecturer.models import Subject
from accounts.models import User


# ! Account and Authentication yet to be added
class Student(models.Model):
    level_choices = [("ND1", "ND1"), ("ND2", "ND2"), ("ND3", "ND3"),
                     ("HND1", "HND1"), ("HND2", "HND2"), ("HND3", "HND3")]
    session_type_choices = [("Full-Time", "Full-Time"),
                            ("Part-Time", "Part-Time")]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    surname = models.CharField(max_length=25)
    first_name = models.CharField(max_length=25)
    other_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    matric_no = models.CharField(max_length=25, null=False)
    session_type = models.CharField(
        choices=session_type_choices, max_length=15, null=False, blank=False)
    level = models.CharField(choices=level_choices,
                             max_length=4, null=False, blank=False)
    # ? related name to access students from subject object
    subjects = models.ManyToManyField(Subject, related_name='students')

    def __str__(self):
        return f"{self.surname} {self.first_name}"
