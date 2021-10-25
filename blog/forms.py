from django import forms
from .models import Post
from .models import Comment
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    textinfo = forms.CharField(label='О чем ваша статья? (коротко)', widget=forms.Textarea, max_length=400)

    class Meta:
        model = Post
        fields = ('title', 'text', 'textinfo',)


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

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
