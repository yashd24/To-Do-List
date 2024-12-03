from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class CustomUser(AbstractUser):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200, unique=True)
    username = models.CharField(max_length=50, unique=True)

    groups = models.ManyToManyField(
        'auth.Group', related_name='CustomUser', blank=True)
    user_permissions = models.ManyToManyField(
        'auth.Permission', related_name='CustomUser', blank=True)

    def __str__(self):
        return self.username


class ToDoItems(models.Model):
    status_choices = [
        ('OPEN', 'Open'),
        ('WORKING', 'Working'),
        ('PENDING REVIEW', 'Pending Review'),
        ('COMPLETED', 'Completed'),
        ('OVERDUE', 'Overdue'),
        ('CANCELLED', 'Cancelled'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(max_length=1000, null=False)
    due_date = models.DateField(null=False, blank=True)
    tags = models.JSONField(default=list, blank=True)
    status = models.CharField(
        max_length=50, choices=status_choices, default='OPEN')

    def save(self, *args, **kwargs):
        self.tags = list(set(self.tags))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
