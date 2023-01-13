from django.forms import ModelForm, forms, TextInput,Textarea,Select,CharField,ModelChoiceField
from .models import Quiz
from lecturer.models import Subject


class QuizCreationForm(ModelForm):
    title=CharField(widget=TextInput(attrs={'class':'form-control'}))
    description=CharField(widget=Textarea(attrs={'class':'form-control'}))
    subject=ModelChoiceField(queryset=Subject.objects.all(), widget=Select(attrs={'class':'form-control'}))
    class Meta:
        model = Quiz
        fields = ("title", "description", "subject")
        
