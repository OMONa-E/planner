from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


# User model -- customize 
class User(AbstractUser):
    pass


# Agent model
class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


# Plan model
class Plan(models.Model):
    CATEGORY = (
        ('Business', 'Business'),
        ('Personal', 'Personal'),
        ('Other', 'Other'),
        ('Home', 'Home'),
        ('Work', 'Work')                
    )
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY)
    image = models.ImageField(blank=True, null=True, upload_to='static/media/image/%Y/%m/%d')
    special_file = models.FileField(blank=True, null=True, upload_to='static/media/special_file/%Y/%m/%d')
    notify = models.DateTimeField(default=datetime.now)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


# Pin model
class Pin(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
