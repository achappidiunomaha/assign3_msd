from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
from django.forms.widgets import DateInput
from ski.models import *


class ClientSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password1", "password2")

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_client = True
        user.save()
        Client.objects.create(user=user)
        return user


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('address', 'city', 'state', 'zipcode', 'phone')



# class RequestForm(forms.ModelForm):
#     class Meta:
#         model = Request
#         fields = ()
