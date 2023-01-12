from django import forms

class SignInForm(forms.Form):
    username = forms.CharField(max_length = 75, widget=forms.TextInput(attrs={'autocomplete':'off', 'placeholder':'Enter Your Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete':'off', 'placeholder':'Enter Your Password'}))


    
