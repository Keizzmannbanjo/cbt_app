from django.forms import ModelForm, Form, TextInput,Textarea,Select,CharField,ModelChoiceField
from .models import Quiz
from lecturer.models import Subject


class QuizCreationForm(ModelForm):
    title=CharField(widget=TextInput(attrs={'class':'form-control'}))
    description=CharField(widget=Textarea(attrs={'class':'form-control'}))
    class Meta:
        model = Quiz
        fields = ("title", "description")
        



