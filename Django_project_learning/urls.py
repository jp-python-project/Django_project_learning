"""
URL configuration for Django_project_learning project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from userlogin.views import RegisterView
from django.contrib.auth import views as auth_views
from userlogin.views import CustomLoginView
from userlogin.forms import LoginForm
from userlogin.views import ResetPasswordView
from website.views import welcome

urlpatterns = [
    path('admin/', admin.site.urls),
    path('meetings/', include('Test_Meeting.urls')),
    path('welcome/', welcome, name='welcome'),
    path('SignUp/', RegisterView.as_view(), name='users-register'),
    path('', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='users/login.html',
                                     authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
]
