#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=========================================================================================================
Project: Python Expense Tracker (Django)
File: src/apps/__init__.py
Author: Mobin Yousefi (GitHub: https://github.com/mobinyousefi-cs)
Created: 2025-10-19
Updated: 2025-10-19
License: MIT License (see LICENSE file for details)
=========================================================================================================

Top-level package for all local Django apps (accounts, expenses, dashboard).
This file intentionally exposes minimal metadata for clarity.
"""
from __future__ import annotations

__all__: list[str] = ["LOCAL_APPS", "__version__"]

LOCAL_APPS: tuple[str, ...] = (
    "apps.accounts",
    "apps.expenses",
    "apps.dashboard",
)
__version__: str = "0.1.0"