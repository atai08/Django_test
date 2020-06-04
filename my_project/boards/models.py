from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField() #-> description TextField NOT NULL

    def __str__(self):
        return self.name



class Topic(models.Model):
    subject = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='topics')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topics')

    def __str__(self):
        return self.subject


class Post(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='posts')
    message = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    authored_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    moderated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+', null=True, blank=True)

