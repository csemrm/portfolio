from django.contrib import admin

from .models import (
    Contact,
    Project,
    ProjectImage
)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']
    search_fields = ['name', 'email', 'phone']


class ProjectImageInline(admin.StackedInline):
    model = ProjectImage
    fields = ('title', 'image')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'summery', 'url', 'release_date','number_screen_uploaded']
    list_display_links = ["title", "release_date"]
    search_fields = ['title', 'url']
    inlines = [
        ProjectImageInline
    ]
    fieldsets = [
        (
            None,
            {
                "fields": ["title", "url", "release_date", "summery"],
            },
        ),
        (
            "More Information",
            {
                "classes": ["wide"],
                "fields": ["description"],
            },
        ),
    ]




admin.site.register(Contact, ContactAdmin)
admin.site.register(Project,ProjectAdmin)