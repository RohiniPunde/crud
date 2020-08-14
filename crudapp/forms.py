from django.forms import ModelForm
from .models import Customer
from django.contrib.auth.forms import UserCreationForm
from django.contrib .auth .models import User
from django import forms


class CustomerForm(ModelForm):
    class Meta:
        model=Customer
        fields= '__all__'