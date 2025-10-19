#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""User profile model extending Django User."""
from __future__ import annotations
from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    class IncomeFrequency(models.TextChoices):
        DAILY = "DAILY", "Daily"
        WEEKLY = "WEEKLY", "Weekly"
        MONTHLY = "MONTHLY", "Monthly"

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    base_income = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    savings_goal = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    income_frequency = models.CharField(
        max_length=16, choices=IncomeFrequency.choices, default=IncomeFrequency.MONTHLY
    )

    def __str__(self) -> str:  # pragma: no cover
        return f"Profile({self.user.username})"
