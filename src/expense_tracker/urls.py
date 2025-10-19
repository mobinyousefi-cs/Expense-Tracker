#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Project URL configuration."""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("apps.accounts.urls")),
    path("expenses/", include("apps.expenses.urls")),
    path("dashboard/", include("apps.dashboard.urls")),
    path("", RedirectView.as_view(pattern_name="dashboard:index", permanent=False)),
]