# tasks/urls.py

from django.urls import path
from .views import UserCreateView, UserListView, TaskCreateView, UserTaskListView

urlpatterns = [
    path("users/", UserCreateView.as_view(), name="user-create"),
    path("users/list/", UserListView.as_view(), name="user-list"),
    path("tasks/", TaskCreateView.as_view(), name="task-create"),
    path(
        "users/<int:user_id>/tasks/", UserTaskListView.as_view(), name="user-tasks-list"
    ),
]
