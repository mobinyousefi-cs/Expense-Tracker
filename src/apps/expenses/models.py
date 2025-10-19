from __future__ import annotations
from django.conf import settings
from django.db import models


class Expense(models.Model):
    class Kind(models.TextChoices):
        INFLOW = "INFLOW", "Inflow"
        OUTFLOW = "OUTFLOW", "Outflow"

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    kind = models.CharField(max_length=10, choices=Kind.choices, default=Kind.OUTFLOW)
    category = models.CharField(max_length=64)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date", "-created_at"]

    def __str__(self) -> str:  # pragma: no cover
        return f"{self.kind} {self.amount} {self.category} ({self.date})"


