from django.urls import path, include
from . import views

urlpatterns = [
    path("login/", views.AdminLoginView.as_view()),
    path("create/", views.CreateUser.as_view()),
    path("morabi/", views.GetMorabi.as_view()),
    path("class/", views.ClassView.as_view()),
]
