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

class ExecutorForm(forms.ModelForm):
    class Meta:
        model = Executor
        fields = ['fullname', 'photo', 'bio', 'skills']


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['fullname', 'email', 'category', 'project_description', 'attachment']
        labels = {
            'fullname': 'ФИО',
            'email': 'Email',
            'category': 'Категория',
            'project_description': 'Описание проекта',
            'attachment': 'Тех. задание'
        }
        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': True}),
            'project_description': forms.Textarea(attrs={'class': 'form-control','rows': 5, 'required': True}),
            'attachment': forms.FileInput(attrs={'class': 'form-control', 'required': True})
        }
        category = forms.ModelChoiceField(queryset=DesignCategory.objects.all(), widget=forms.Select(attrs={'class': 'form-control', 'required': True}))

class RequestCreateView(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['fullname', 'email', 'category', 'project_description', 'attachment']


class OrderAssignmentForm(forms.ModelForm):
    class Meta:
        model = ClientOrder
        fields = ['assigned_executor', 'status']
        labels = {
            'assigned_executor': 'Выберите исполнителя',
            'status': 'Статус',
        }
        widgets = {
            'assigned_executor': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }




