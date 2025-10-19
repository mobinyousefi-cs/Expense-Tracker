from __future__ import annotations
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SignUpForm, ProfileForm
from .models import UserProfile


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data["email"]
            user.save()
            UserProfile.objects.create(
                user=user,
                base_income=form.cleaned_data["base_income"],
                savings_goal=form.cleaned_data["savings_goal"],
                income_frequency=form.cleaned_data["income_frequency"],
            )
            login(request, user)
            messages.success(request, "Welcome! Your profile has been created.")
            return redirect("dashboard:index")
    else:
        form = SignUpForm()
    return render(request, "accounts/signup.html", {"form": form})


@login_required
def profile(request):
    profile = request.user.profile
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated.")
            return redirect("accounts:profile")
    else:
        form = ProfileForm(instance=profile)
    return render(request, "accounts/profile.html", {"form": form})