from django.urls import path, include
from . import views

urlpatterns = [
    path("login/", views.AdminLoginView.as_view()),
    path("create/", views.CreateUser.as_view()),
    path("users/", views.UsersView.as_view()),
    path("morabi/", views.GetMorabi.as_view()),
    path("morabi/", views.GetMorabi.as_view()),
    path("class/", views.ClassView.as_view()),
    path('class/<int:class_id>/users/', views.ClassUserView.as_view(), name='class_users'),
    path('class/<int:class_id>/users/<int:user_id>/', views.ClassUserView.as_view(), name='class_user_delete'),
]
