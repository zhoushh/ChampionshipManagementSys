from django.urls import path,include,re_path
from . import views
from django.contrib.auth import views as authViews

app_name = 'user'

urlpatterns = [
    path("login/", views.loginView, name='loginView'),
    path("register/", views.registerView, name='registerView'),
    path("logout/", authViews.logout, name='logoutView')
]