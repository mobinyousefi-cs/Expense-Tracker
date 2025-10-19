from __future__ import annotations
from datetime import date, timedelta
from collections import defaultdict
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import render
from apps.expenses.models import Expense


@login_required
def index(request):
    return render(request, "dashboard/index.html")


@login_required
def chart_data(request):
    """Return JSON for weekly, monthly, yearly category sums (separate inflow/outflow)."""
    today = date.today()

    # date ranges
    start_week = today - timedelta(days=today.weekday())  # monday
    start_month = today.replace(day=1)
    start_year = today.replace(month=1, day=1)

    def aggregate(start: date):
        qs = (
            Expense.objects.filter(user=request.user, date__gte=start, date__lte=today)
            .values("category", "kind")
            .annotate(total=Sum("amount"))
        )
        data = defaultdict(lambda: {"INFLOW": 0, "OUTFLOW": 0})
        for row in qs:
            data[row["category"]][row["kind"]] = float(row["total"])
        # Convert to lists per kind
        cats = sorted(data.keys())
        inflow = [data[c]["INFLOW"] for c in cats]
        outflow = [data[c]["OUTFLOW"] for c in cats]
        return {"categories": cats, "inflow": inflow, "outflow": outflow}

    payload = {
        "weekly": aggregate(start_week),
        "monthly": aggregate(start_month),
        "yearly": aggregate(start_year),
    }
    return JsonResponse(payload)