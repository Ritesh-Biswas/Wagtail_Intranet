from django.contrib.auth.models import Group
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def create_default_roles(sender, **kwargs):
    """Creates default user roles in Wagtail's Group model after migrations."""
    default_roles = [
        "Admin",
        "Department Admin",
        "HR Manager",
        "HR Generalist",
        "General User",
    ]
    for role_name in default_roles:
        role, created = Group.objects.get_or_create(name=role_name)
        if created:
            print(f'Role "{role_name}" created')
        else:
            print(f'Role "{role_name}" already exists')
