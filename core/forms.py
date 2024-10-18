from django import forms
from .models import User, Plan, Pin, Agent


class PlanModelForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = [ 'title', 'content', 'category', 'image', 'special_file', 'notify', 'agent' ]


class PinModelForm(forms.ModelForm):
    class Meta:
        model = Pin
        fields = [ 'plan', 'agent', 'content' ]