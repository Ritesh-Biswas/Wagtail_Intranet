from django.shortcuts import render, redirect
from wagtail.models import Page
from .models import DepartmentPage
from .forms import DepartmentForm

def create_department(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            department = form.save(commit=False)
            # Assign the parent page (assuming the homepage is the parent)
            homepage = Page.objects.get(slug="home")
            department.parent = homepage
            department.save()
            return redirect("/")  # Redirect to homepage after creation
    else:
        form = DepartmentForm()

    return render(request, "departments/create_department.html", {"form": form})
