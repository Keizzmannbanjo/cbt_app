from django.db import models


from lecturer.models import Subject
from accounts.models import User 



# ! Account and Authentication yet to be added
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    surname = models.CharField(max_length=25)
    first_name = models.CharField(max_length=25)
    other_name = models.CharField(max_length=25)
    email = models.EmailField()
    matric_no = models.CharField(max_length=25, null=False)
    subjects =models.ManyToManyField(Subject, related_name='students') # ? related name to access students from subject object

    def __str__(self):
        return f"{self.surname} {self.first_name}"
    
