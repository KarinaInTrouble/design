from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['fullname', 'subject', 'message', 'email']
        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': True}),
        }
        labels = {
            'fullname': 'ФИО',
            'subject': 'Тема',
            'message': 'Текст',
            'email': 'Email',
        }

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Обязательное поле. Введите действующий адрес электронной почты.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



