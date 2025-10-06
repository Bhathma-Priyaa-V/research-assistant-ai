from rest_framework.routers import DefaultRouter
from .views import ResearchPaperViewSet

router = DefaultRouter()
router.register(r'papers', ResearchPaperViewSet)

urlpatterns = router.urls
