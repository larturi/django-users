from django.urls import path
from . import views

app_name = 'users_app'

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('mixin/', views.TemplatePruebaMixin.as_view(), name='mixin'),
    path('authenticated/', views.AuthenticatedView.as_view(), name='authenticated'),
    path('error/', views.ErrorView.as_view(), name='error'),
]
