from __future__ import annotations
from datetime import date
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
import csv
from .models import Expense
from .forms import ExpenseForm


@login_required
def index(request):
    qs = Expense.objects.filter(user=request.user)
    start = request.GET.get("start")
    end = request.GET.get("end")
    if start:
        qs = qs.filter(date__gte=start)
    if end:
        qs = qs.filter(date__lte=end)
    return render(request, "expenses/index.html", {"expenses": qs, "start": start, "end": end})


@login_required
def create(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            exp = form.save(commit=False)
            exp.user = request.user
            exp.save()
            return redirect("expenses:index")
    else:
        form = ExpenseForm(initial={"date": date.today()})
    return render(request, "expenses/form.html", {"form": form, "title": "Add Record"})


@login_required
def edit(request, pk: int):
    exp = get_object_or_404(Expense, pk=pk, user=request.user)
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=exp)
        if form.is_valid():
            form.save()
            return redirect("expenses:index")
    else:
        form = ExpenseForm(instance=exp)
    return render(request, "expenses/form.html", {"form": form, "title": "Edit Record"})


@login_required
def delete(request, pk: int):
    exp = get_object_or_404(Expense, pk=pk, user=request.user)
    if request.method == "POST":
        exp.delete()
        return redirect("expenses:index")
    return render(request, "expenses/confirm_delete.html", {"expense": exp})


@login_required
def export_csv(request):
    qs = Expense.objects.filter(user=request.user).order_by("date")
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="expenses.csv"'
    writer = csv.writer(response)
    writer.writerow(["date", "kind", "category", "amount", "notes"])
    for e in qs:
        writer.writerow([e.date.isoformat(), e.kind, e.category, f"{e.amount}", e.notes])
    return response