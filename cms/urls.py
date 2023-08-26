from django.urls import include, path
from rest_framework import routers

from cms.views import GalactiveUserLoginView, PriceCalculationView, TumorDetectionViewSet

router = routers.DefaultRouter()
router.register(r"tumor_detection", TumorDetectionViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("galactic-auth", GalactiveUserLoginView.as_view()),
    path("price-calculation", PriceCalculationView.as_view()),
]
