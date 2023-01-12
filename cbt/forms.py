from django.forms import ModelForm, forms
from .models import Quiz


class QuizCreationForm(ModelForm):
    class Meta:
        model = Quiz
        fields = ("title", "description", "subject")
