from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Profile


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput())
    agree_to_terms = forms.BooleanField(
        required=True,
        label='Я соглашаюсь с обработкой персональных данных',
        error_messages={'required': 'Вы должны согласиться с политикой обработки персональных данных.'}
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    # Не работает? Все показывает, но это поле нет.
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput())
    email = forms.EmailField(required=True,
                             widget=forms.TextInput())

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput())
    bio = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']