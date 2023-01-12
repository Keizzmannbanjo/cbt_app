from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    user_type_choice = (
        ('student','Student'),
        ('lecturer','Lecturer'),
        ('registrar','Registrar'),
    )

    type = models.CharField(choices=user_type_choice, null=False, max_length=13, default='registrar')
