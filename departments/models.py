from django.db import models
from wagtail.admin.panels import FieldPanel,InlinePanel
from wagtail.models import Page, Orderable
from django.contrib.auth.models import User
from modelcluster.fields import ParentalKey

class DepartmentPage(Page):
    template = "departments/department_page.html"
    name = models.CharField(max_length=255, help_text="Enter department name")
    description = models.TextField(blank=True, help_text="Provide a brief description")

    # Site Admin: ForeignKey to User, filtering out Admins
    site_admin = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to=~models.Q(groups__name="Admin"),  # Exclude Admins
        related_name="department_admins",
        help_text="Select a Site Admin (excluding Admins)",
    )

    content_panels = Page.content_panels + [
        FieldPanel("name"),
        FieldPanel("description"),
        FieldPanel("site_admin"),
        InlinePanel("announcements", label="Announcements"),  # Add this line
    ]

    parent_page_types = ["wagtailcore.Page"]  # Can be created under the main site
    subpage_types = ['departments.AnnouncementPage']  # Allowing AnnouncementPage as subpage

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"    


class AnnouncementPage(Page):
    template = "departments/announcement_page.html"
    
    announcement_title = models.CharField(
        max_length=255,
        help_text="Title of the announcement"
    )
    announcement_content = models.TextField(
        help_text="Content of the announcement"
    )
    date_posted = models.DateTimeField(auto_now_add=True)

    content_panels = Page.content_panels + [
        FieldPanel("announcement_title"),
        FieldPanel("announcement_content"),
    ]

    parent_page_types = ['departments.DepartmentPage']  # Can only be created under DepartmentPage
    subpage_types = []  # No subpages allowed under AnnouncementPage

    def __str__(self):
        return self.announcement_title

    class Meta:
        verbose_name = "Announcement"
        verbose_name_plural = "Announcements"    

class DepartmentAnnouncement(Orderable):
    page = ParentalKey(DepartmentPage, on_delete=models.CASCADE, related_name='announcements')
    title = models.CharField(max_length=255)
    message = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    
    panels = [
        FieldPanel('title'),
        FieldPanel('message'),
    ]

    def __str__(self):
        return f"{self.title} - {self.date_posted.strftime('%Y-%m-%d')}"
