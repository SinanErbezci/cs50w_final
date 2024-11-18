from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import User 

class NameForm(forms.Form):
    your_name = forms.CharField(label="your name", max_length=100)

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

class CreateUserFrom(UserCreationForm):
    template_name = "library/form_snippet.html"
    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")
