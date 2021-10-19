from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login

from .forms import LoginForm, UserRegisterForm
from .models import User
class UserRegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = '/success'

    def form_valid(self, form):

        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            first_name = form.cleaned_data['first_name'],
            last_name = form.cleaned_data['last_name'],
            gender = form.cleaned_data['gender'],
        )

        return super(UserRegisterView, self).form_valid(form)

class LoginView(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = '/success'

    def form_valid(self, form):
        user = authenticate(
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )

        try:
            login(self.request, user)
        except:
          print('An exception occurred')

        return super(LoginView, self).form_valid(form)

class SuccessView(TemplateView):    
    template_name = 'success.html'

class ErrorView(TemplateView):    
    template_name = 'error.html'
