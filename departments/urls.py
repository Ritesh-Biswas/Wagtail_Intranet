from django.urls import path
from .views import create_department

urlpatterns = [
    path("create/", create_department, name="create_department"),
]
