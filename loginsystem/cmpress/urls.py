from django.contrib import admin
from django.urls import path, include
from cmpress import views

urlpatterns = [
    path('', views.begin, name='begin'),
    path('new/', views.new, name='home'),
    path('login/', views.login_, name="login"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logout_, name="logout"),
    path('otp/', views.otp, name="otp"),
    path('loginnext/', views.file_upload_view,name="afterlogin"),
    path('success/', views.success, name="success"),
    path('success_im/', views.success_im, name="success_im"),
    path('downloadfile_comp/', views.downloadfile_comp, name='downloadfile_comp'),
    path('downloadfile_decomp/', views.downloadfile_decomp, name='downloadfile_decomp'),
    path('downloadfile_im/', views.downloadfile_im, name='downloadfile_im'),

]
