#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Basic model tests."""
import datetime as _dt
import pytest
from django.contrib.auth.models import User
from apps.expenses.models import Expense

pytestmark = pytest.mark.django_db


def test_expense_str():
    u = User.objects.create_user("alice", password="x")
    e = Expense.objects.create(user=u, kind=Expense.Kind.OUTFLOW, category="Food", amount=10, date=_dt.date.today())
    s = str(e)
    assert "Food" in s and "10" in s
