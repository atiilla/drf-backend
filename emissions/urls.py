from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import SourceViewSet, ModificationViewSet, StrategyViewSet, ReportViewSet

router = DefaultRouter()
router.register(r'reports', ReportViewSet)
router.register(r'sources', SourceViewSet)
router.register(r'modifications', ModificationViewSet)
router.register(r'strategies', StrategyViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]

urlpatterns = router.urls