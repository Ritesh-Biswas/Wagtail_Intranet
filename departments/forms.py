from django import forms
from .models import DepartmentPage
from django.contrib.auth.models import User

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = DepartmentPage
        fields = ["title", "name", "description", "site_admin"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter site_admin field to exclude users in the Admin group
        self.fields["site_admin"].queryset = User.objects.exclude(groups__name="Admin")
