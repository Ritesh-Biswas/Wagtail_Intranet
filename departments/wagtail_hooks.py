from wagtail import hooks
from wagtail.admin.menu import MenuItem
from django.urls import reverse
from wagtail.models import Page

@hooks.register("register_admin_menu_item")
def register_department_menu():
    return MenuItem(
        "Departments", 
        reverse("wagtailadmin_explore", args=[Page.objects.get(slug='react').id]),
        # reverse("create_department"),
        icon_name="group",
        order=200
    )