from django.contrib import admin
from .models import User, Agent, Pin, Plan


# Register your models here.
admin.site.register( (Agent, Plan, Pin, User) )