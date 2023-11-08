from django.urls import path
from . import views

urlpatterns = [
    path("home", views.home, name="home"),
    path("create-todo/", views.create_todo, name="create_todo"),
    path('post/<int:pk>/delete/', views.delete_todo, name='delete_todo')

]