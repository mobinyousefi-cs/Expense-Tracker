#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=========================================================================================================
Project: Python Expense Tracker (Django)
File: src/apps/accounts/__init__.py
Author: Mobin Yousefi (GitHub: https://github.com/mobinyousefi-cs)
Created: 2025-10-19
Updated: 2025-10-19
License: MIT License (see LICENSE file for details)
=========================================================================================================

Accounts app package. Contains signup, login/logout, and profile management.
"""
from __future__ import annotations

__all__: list[str] = ["__version__", "APP_NAME"]

APP_NAME: str = "accounts"
__version__: str = "0.1.0"