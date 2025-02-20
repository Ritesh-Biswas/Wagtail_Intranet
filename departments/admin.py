from django.contrib import admin
from wagtail_modeladmin.options import ModelAdmin, modeladmin_register 
from .models import DepartmentPage

@modeladmin_register
class DepartmentPageAdmin(ModelAdmin):
    model = DepartmentPage
    menu_label = 'Departments'  # Text that appears in the menu
    menu_icon = 'folder'  # Icon that appears in the menu
    menu_order = 200
    list_display = ('name', 'site_admin', 'description')
    search_fields = ('name', 'description')
    list_filter = ('site_admin',)

# @modeladmin_register
# class AnnouncementPageAdmin(ModelAdmin):
#     model = AnnouncementPage
#     menu_label = 'Announcements'
#     menu_icon = 'doc-full'
#     menu_order = 201
#     list_display = ('announcement_title', 'date_posted')
#     search_fields = ('announcement_title', 'announcement_content')
#     list_filter = ('date_posted',)

# admin.site.register(DepartmentAnnouncement)
# admin.site.register(AnnouncementPage)
admin.site.register(DepartmentPage)