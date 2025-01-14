from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE) # Links to Django's User model
    bio = models.TextField(max_length=500, blank=True) # Additional field for user bio

class Post(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE) # Links to Django's User model
    title = models.CharField(max_length=100)
    content = models.TextField() # Title of post
    created_at = models.DateTimeField(auto_now_add=True) # Automatically set to current date and time when the post is created

class Comment(models.Model):
    author = models.CharField(max_length=100) # Name of Commenter
    post = models.ForeignKey(Post, related_name='comments', on_delete = models.CASCADE) # Links to Post model
    body = models.TextField() #The body of the comment
    created_at = models.DateTimeField(auto_now_add=True) # Automatically set to current date and time when the comment is created