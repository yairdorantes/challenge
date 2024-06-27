from django.shortcuts import render

from rest_framework import generics
from .models import User, Task
from .serializers import UserSerializer, TaskSerializer


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class UserTaskListView(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        return Task.objects.filter(user_id=user_id)
