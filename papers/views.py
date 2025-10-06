from rest_framework import viewsets
from .models import ResearchPaper
from .serializers import ResearchPaperSerializer

class ResearchPaperViewSet(viewsets.ModelViewSet):
    queryset = ResearchPaper.objects.all().order_by("-created_at")
    serializer_class = ResearchPaperSerializer
