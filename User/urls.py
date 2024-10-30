from django.urls import path, include
from . import views

urlpatterns = [
    path("login/", views.UserLoginView.as_view()),
    path("data/", views.GetUserView.as_view()),
    path("class/", views.UserClassesView.as_view()),
]
