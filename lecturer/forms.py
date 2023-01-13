from django.db import transaction

from django import forms 
from accounts.models import User
from .models import Lecturer,Subject

class LecturerCreationForm(forms.ModelForm):
    class Meta:
        model = Lecturer
        fields = ('surname','first_name', 'other_name','subject', 'email')
        widget = {
            'surname':forms.TextInput(attrs={'autocomplete':'off'}),
            'first_name':forms.TextInput(attrs={'autocomplete':'off'}),
            'other_name':forms.TextInput(attrs={'autocomplete':'off'}),
            'email':forms.TextInput(attrs={'autocomplete':'off'}),
        }

  

    @transaction.atomic
    def save(self):
        lecturer = super().save(commit=False)
        user = User.objects.create_user(username = self.cleaned_data.get('first_name'), email = self.cleaned_data.get('email'),type = 'lecturer', password = self.cleaned_data.get('surname'))
        user.save()
        lecturer.user = user 
        lecturer.subject = Subject.objects.get(title = self.cleaned_data.get('subject'))
        lecturer.save()
        

class SubjectCreationForm(forms.ModelForm):
    class Meta:
        model = Subject 
        fields = "__all__"