from django.db import models
from django.db import models


class User(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, related_name="tasks", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
