from django.urls import path
from . import views

app_name = 'users_app'

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='user-register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('error/', views.ErrorView.as_view(), name='error'),
]
