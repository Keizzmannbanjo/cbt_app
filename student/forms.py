from django import forms
from django.db import transaction

from .models import Student
from accounts.models import User
from lecturer.models import Subject


class StudentCreationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['surname', 'first_name', 'other_name','email','matric_no','subjects']
        widgets = {
            'subjects': forms.CheckboxSelectMultiple
        }
        
        


    @transaction.atomic
    def save(self):
        student = super().save(commit=False)
        user = User.objects.create_user(username = self.cleaned_data.get('surname'),email = self.cleaned_data.get('email'),password = self.cleaned_data.get('matric_no'), type = 'student')
        subjects = self.cleaned_data.get('subjects')
        user.save()
        student.user = user 
        student.save()
        for subject in subjects:
            student.subjects.add(subject)
        student.save()