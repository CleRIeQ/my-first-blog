from django import forms
from django.forms.widgets import TextInput
from .models import Category, Post
from .models import Comment
from django.contrib.auth.models import User

choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    textinfo = forms.CharField(label='Описание', widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=250)
    text = forms.CharField(label='Текст', widget=forms.Textarea(), max_length=10000)
    title = forms.CharField(label='Название', widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=200)
    category = forms.ChoiceField(choices=choices, label='Категории')

    class Meta:
        model = Post
        fields = ('title', 'text', 'textinfo', 'category')


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повтор', widget=forms.PasswordInput)
    email = forms.CharField(label='email', widget=forms.TextInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class LoginUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    username= forms.CharField(label='Логин', widget=TextInput)

    class Meta:
        model = User
        fields = {'username', 'password'}