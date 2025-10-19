#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime as _dt
import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from apps.expenses.models import Expense

pytestmark = pytest.mark.django_db


def login(client):
    user = User.objects.create_user("bob", password="secret")
    client.login(username="bob", password="secret")
    return user


def test_dashboard_requires_login(client):
    resp = client.get(reverse("dashboard:index"))
    assert resp.status_code == 302  # redirect to login


def test_add_expense_flow(client):
    user = login(client)
    resp = client.post(reverse("expenses:add"), {
        "kind": "OUTFLOW",
        "category": "Transport",
        "amount": 5,
        "date": _dt.date.today(),
        "notes": "bus",
    })
    assert resp.status_code == 302
    assert Expense.objects.filter(user=user, category="Transport").exists()
