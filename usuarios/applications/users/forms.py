from django import forms
from django.contrib.auth import authenticate

from .models import User

class LoginForm(forms.Form):

    email = forms.CharField(
        label='Email',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Email',
                'class': 'input'
            }
        )
    )

    password = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
                'class': 'input'
            }
        )
    )

    def clean(self):

        cleaned_data = super(LoginForm, self).clean()

        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        if not authenticate(email=email, password=password):
            raise forms.ValidationError('Usuarios / Clave Incorrectos')

        return self.cleaned_data

class UserRegisterForm(forms.ModelForm):

    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    )

    email = forms.CharField(
        label='Email',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Email',
                'class': 'input'
            }
        )
    )

    username = forms.CharField(
        label='Username',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Username',
                'class': 'input'
            }
        )
    )

    first_name = forms.CharField(
        label='Nombre',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Nombre',
                'class': 'input'
            }
        )
    )

    last_name = forms.CharField(
        label='Apellido',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Apellido',
                'class': 'input'
            }
        )
    )

    gender = forms.CharField(
        label='Genero',
        required=True,
        widget=forms.Select(
            choices=GENDER_CHOICES,
            attrs={
                'placeholder': 'Genero',
                'class': 'input'
            }
        )
    )


    password1 = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
                'class': 'input'
            }
        )
    )

    password2 = forms.CharField(
        label='Repetir Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repetir Password',
                'class': 'input'
            }
        )
    )
    
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'gender',
        )

    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseñas no coinciden')
