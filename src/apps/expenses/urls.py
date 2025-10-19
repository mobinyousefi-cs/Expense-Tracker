from django.urls import path
from . import views

app_name = "expenses"

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.create, name="add"),
    path("<int:pk>/edit/", views.edit, name="edit"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("export/", views.export_csv, name="export"),
]