from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page
from django.contrib.auth.models import User

class DepartmentPage(Page):
    template = "departments/department_page.html"
    name = models.CharField(max_length=255, help_text="Enter department name")
    description = models.TextField(blank=True, help_text="Provide a brief description")

    site_admin = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to=~models.Q(groups__name="Admin"),
        related_name="department_admins",
        help_text="Select a Site Admin (excluding Admins)",
    )

    content_panels = Page.content_panels + [
        FieldPanel("name"),
        FieldPanel("description"),
        FieldPanel("site_admin"),
    ]

    parent_page_types = ["wagtailcore.Page"]
    subpage_types = ['departments.AnnouncementSectionPage']  # Only allow AnnouncementSection as subpage

    def __str__(self):
        return self.name

class AnnouncementSectionPage(Page):
    template = "departments/announcement_section.html"
    
    description = models.TextField(
        blank=True,
        help_text="Description of this announcement section"
    )

    content_panels = Page.content_panels + [
        FieldPanel("description"),
    ]

    parent_page_types = ['departments.DepartmentPage']  # Can only be created under Department
    subpage_types = ['departments.SubAnnouncementPage']  # Only allow SubAnnouncement as subpage

    class Meta:
        verbose_name = "Announcement Section"
        verbose_name_plural = "Announcement Sections"

class SubAnnouncementPage(Page):
    template = "departments/sub_announcement.html"
    
    announcement_content = models.TextField(
        help_text="Content of the announcement"
    )
    date_posted = models.DateTimeField(auto_now_add=True)

    content_panels = Page.content_panels + [
        FieldPanel("announcement_content"),
    ]

    parent_page_types = ['departments.AnnouncementSectionPage']  # Can only be created under AnnouncementSection
    subpage_types = []  # No subpages allowed

    class Meta:
        verbose_name = "Announcement"
        verbose_name_plural = "Announcements"