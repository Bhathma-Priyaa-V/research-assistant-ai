from django.contrib import admin
from .models import ResearchPaper

@admin.register(ResearchPaper)
class ResearchPaperAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "sha256")
    search_fields = ("title", "sha256")
