import datetime

from django.shortcuts import render
from django.core.mail import send_mail
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.views.generic import View, CreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from .functions import code_generator

from .forms import (
    LoginForm, 
    UserRegisterForm, 
    UpdatePasswordForm,
    VerificationForm
)

from .models import User
class UserRegisterView(FormView):

    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users_app:authenticated')

    def form_valid(self, form):

        # Codigo de verificacion de registro
        codigo = code_generator()

        usuario = User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            first_name = form.cleaned_data['first_name'],
            last_name = form.cleaned_data['last_name'],
            gender = form.cleaned_data['gender'],
            code_register = codigo
        )

        # Enviar el codigo al email del usuario
        asunto = 'Confirmacion de email'
        mensaje = 'Codigo de verificacion: ' + codigo
        remitente = 'lea.arturi.drive@gmail.com'

        send_mail(asunto, mensaje, remitente, [form.cleaned_data['email']])

        # Redireccion a vista de validacion

        return HttpResponseRedirect(
            reverse(
                'users_app:verification',
                kwargs={'pk':usuario.id}
            )
        )


class LoginView(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('users_app:authenticated')

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

class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse('users_app:login')
        )

class FechaMixin(object):

    def get_context_data(self, **kwargs):
        context = super(FechaMixin, self).get_context_data(**kwargs)
        context['fecha'] = datetime.datetime.now()
        return context

class TemplatePruebaMixin(FechaMixin, TemplateView):
    template_name = 'users/mixin.html'

class AuthenticatedView(LoginRequiredMixin, TemplateView):    
    template_name = 'users/authenticated.html'
    login_url = reverse_lazy('users_app:login')

class UpdatePasswordView(LoginRequiredMixin, FormView):
    template_name = 'users/update-password.html'
    form_class = UpdatePasswordForm
    success_url = reverse_lazy('users_app:login')
    login_url = reverse_lazy('users_app:login')

    def form_valid(self, form):

        usuario = self.request.user

        user = authenticate(
            email = usuario.email,
            password = form.cleaned_data['password_actual'],
        )

        if user:
            new_password = form.cleaned_data['password_nuevo']
            usuario.set_password(new_password)
            usuario.save()

        logout(self.request)

        return super(UpdatePasswordView, self).form_valid(form)

class ErrorView(TemplateView):    
    template_name = 'error.html'

class CodeVerificationView(FormView):

    template_name = 'users/verification.html'
    form_class = VerificationForm
    success_url = reverse_lazy('users_app:login')

    def get_form_kwargs(self):
        kwargs = super(CodeVerificationView, self).get_form_kwargs()
        kwargs.update({
            'pk': self.kwargs['pk']
        })

        return kwargs

    def form_valid(self, form):

        User.objects.filter(
            id=self.kwargs['pk']
        ).update(is_active=True)

        return super(CodeVerificationView, self).form_valid(form)