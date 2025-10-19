from __future__ import annotations
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    base_income = forms.DecimalField(max_digits=12, decimal_places=2, min_value=0)
    savings_goal = forms.DecimalField(max_digits=12, decimal_places=2, min_value=0)
    income_frequency = forms.ChoiceField(choices=UserProfile.IncomeFrequency.choices)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "base_income", "savings_goal", "income_frequency")


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("base_income", "savings_goal", "income_frequency")
