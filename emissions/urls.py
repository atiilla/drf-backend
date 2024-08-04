from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import EmissionSourceViewSet, EmissionAdjustmentViewSet, EmissionStrategyViewSet, AnnualReportViewSet

router = DefaultRouter()
router.register(r'annual-reports', AnnualReportViewSet)
router.register(r'emission-sources', EmissionSourceViewSet)
router.register(r'emission-adjustments', EmissionAdjustmentViewSet)
router.register(r'emission-strategies', EmissionStrategyViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]

urlpatterns = router.urls
