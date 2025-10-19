#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=========================================================================================================
Project: Python Expense Tracker (Django)
File: src/expense_tracker/__init__.py
Author: Mobin Yousefi (GitHub: https://github.com/mobinyousefi-cs)
Created: 2025-10-19
Updated: 2025-10-19
License: MIT License (see LICENSE file for details)
=========================================================================================================

Package initializer for the Django project. Exposes lightweight metadata and a helper to
retrieve the current package version at runtime.
"""
from __future__ import annotations

__all__: list[str] = ["get_version", "__version__", "PROJECT", "AUTHOR"]

PROJECT: str = "Python Expense Tracker (Django)"
AUTHOR: str = "Mobin Yousefi"
__version__: str = "0.1.0"


def get_version() -> str:
    """Return the library version string."""
    return __version__
