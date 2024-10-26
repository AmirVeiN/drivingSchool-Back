from django.urls import path, include
from . import views

urlpatterns = [
    path("login/", views.AdminLoginView.as_view()),
    path("create/", views.CreateUser.as_view()),
]
