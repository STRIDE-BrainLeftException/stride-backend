from django.urls import include, path
from rest_framework import routers

from cms.views import GalactiveUserLoginView

router = routers.DefaultRouter()
# router.register(r"users", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("galactic-auth", GalactiveUserLoginView.as_view()),
]
