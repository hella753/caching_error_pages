from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


app_name="user"
urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegistrationView.as_view(), name='register'),
]
