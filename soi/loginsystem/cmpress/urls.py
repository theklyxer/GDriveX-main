from django.contrib import admin
from django.urls import path, include
from cmpress import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('login/', views.login_, name="loginpage"),
    path('signup/', views.signup, name="signuppage"),
    path('logout/', views.logout_, name="logoutpage")
]