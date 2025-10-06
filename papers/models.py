import uuid
from django.db import models

class ResearchPaper(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=1024, blank=True)
    file = models.FileField(upload_to='papers/')
    sha256 = models.CharField(max_length=64, unique=True)
    text = models.TextField(blank=True)
    summary = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or "Untitled Paper"
