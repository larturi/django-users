from django import forms
from .models import User

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
